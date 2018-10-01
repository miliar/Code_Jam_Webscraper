#!/usr/bin/env python2.6

# Copyright Nate White, 2010

import optparse
import sys

# TODO
# x Get this to work for the middle example test case (one group)
# x Create some test cases to verify that this works well for huge R
# x Correct for the case where the queue is empty

def generate(n):
    import random
    print n
    for i in xrange(n):
        R, k, N = (random.randint(1, 1000), random.randint(1, 1000),
                   random.randint(1, 1000))
        print R, k, N
        for n in xrange(N):
            print random.randint(1, min(k, 10)),
        print

def main():
    parser = optparse.OptionParser()
    parser.set_usage('%prog [options] <file>')
    parser.add_option("-d", "--debug", default=False,
        action="store_true", help="print progress messages to stdout")
    parser.add_option("-g", "--generate", default=None, action="store",
        type="int", metavar="N", help="generate a sample input of N tests")
    parser.add_option("-p", "--profile", default=False, action="store_true",
        help="run with profiling enabled")
    parser.add_option("-v", "--verify", default=False, action="store_true",
        help="verify result against brute-force algorithm")
    (options, args) = parser.parse_args()
    if len(args) != 0:
        print parser.error('Unexpected positional arguments seen')

    if options.generate:
        generate(options.generate)
        return

    if options.profile:
        import cProfile as profile
        profile.runctx("puzzle(options, args)", globals(), locals())
    else:
        puzzle(options, args)

def brute(R, k, g, pos=0, step=None):
    res = 0
    for r in xrange(R):
        spots = k
        startpos = pos
        i = 0
        if step is not None:
            res += step[pos][1]
            pos = step[pos][0]
        else:
            while g[pos] <= spots and (pos != startpos or i == 0):
                i += 1
                res += g[pos]
                spots -= g[pos]
                pos += 1
                pos %= len(g)

    return res

def puzzle(options, args):
    (T,) = ([int(i) for i in sys.stdin.readline().split()])
    for t in xrange(1, T + 1):
        (R, k, N) = ([int(i) for i in sys.stdin.readline().split()])
        orig_R = R
        g = ([int(i) for i in sys.stdin.readline().split()])[:N]
        riders = sum(g)
        if options.debug:
            print "Input:", R, k, N, riders, g

        # Compute the starting group for the next ride for each group, given k
        step = [None] * N
        for n in xrange(N):
            rem = riders
            if riders > k:
                rem = k % riders
            u = 0
            for i in xrange(n, n + N + 1):
                if rem >= g[i % N]:
                    u += g[i % N]
                    rem -= g[i % N]
                else:
                    break
            step[n] = (i % N, u)

        if options.debug:
            print "Steps:", step

        # Now start walking groups, keeping a lookaside table; only <= N times
        mem = {}
        pos = 0
        res = 0
        path = []
        while pos not in mem and R:
            path.append(pos)
            R -= 1
            s = step[pos]
            res += s[1]
            mem[pos] = s[0]
            pos = s[0]

        if R: # If we haven't exhausted R, then we've identified a cycle;
              # we can now brute force for all remaining rides.
            # Identify the cycle and how many full loops of the riders it is
            idx = path.index(pos)
            cycle = len(path) - idx
            last = path[idx]
            loops = 0
            for i in path[idx:] + [path[idx]]:
                if i < last:
                    loops += 1
                last = i

            # Account for all cycles seen
            res += (R // cycle) * riders * max(loops, 1)
            R %= cycle
            if options.debug:
                print "Cycle:", res, cycle, pos, R, loops, path

            # Brute force the remainder; this is fairly cheap
            res += brute(R, k, g, pos, step)

        if options.verify:
            res2 = brute(orig_R, k, g)
            if options.debug:
                print "Results:", res, res2
            assert res == res2

        print 'Case #%d: %d' % (t, res)

if __name__ == '__main__':
    main()

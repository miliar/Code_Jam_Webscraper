#!/bin/env python

def debug_stalls(stalls):
    return
    out = []
    for occupied in stalls:
        if occupied:
            out.append("o")
        else:
            out.append(".")
    print "".join(out)

def bathroom_stalls(n, k):
    stalls = [False] * (n + 2)
    stalls[0] = True
    stalls[-1] = True

    min_maximal = None
    max_maximal = None

    for i in xrange(k):
        empty_scores = []
        for j, occupied in enumerate(stalls):
            if occupied: continue

            k = j
            while stalls[k - 1] == False:
                k -= 1
            Ls = j - k

            k = j
            while stalls[k + 1] == False:
                k += 1
            Rs = k - j

            empty_scores.append((j, Ls, Rs))

        debug_stalls(stalls)
        min_maximal = max(min(Ls, Rs) for (j, Ls, Rs) in empty_scores)
        min_maximals = [
            (j, Ls, Rs)
            for (j, Ls, Rs) in empty_scores
            if min(Ls, Rs) == min_maximal
        ]
        max_maximal = max(max(Ls, Rs) for (j, Ls, Rs) in min_maximals)

        if len(min_maximals) == 1:
            stalls[min_maximals[0][0]] = True
        else:
            max_maximals = [
                j for (j, Ls, Rs) in min_maximals
                if max(Ls, Rs) == max_maximal
            ]

            if len(max_maximals) == 1:
                stalls[max_maximals[0]] = True
            else:
                stalls[max_maximals[0]] = True

    debug_stalls(stalls)
    return (max_maximal, min_maximal)


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]
        y, z = bathroom_stalls(n, k)
        print "Case #{}: {} {}".format(i, y, z)

if __name__ == "__main__":
    main()

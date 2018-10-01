"""
Problem

Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate chips
 on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head cook on duty. The pancakes are cooked in a single row over a hot surface.
As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized
pancake flipper that flips exactly K consecutive pancakes. That is, in that range of K pancakes,
it changes every happy-side pancake to a blank-side pancake, and vice versa; it does not change the
left-to-right order of those pancakes.

You cannot flip fewer than K pancakes at a time with the flipper, even at the ends of the row
(since there are raised borders on both sides of the cooking surface).
For example, you can flip the first K pancakes, but not the first K - 1 pancakes.

Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to
flip some individual pancakes and then ran to the restroom with it, right before the time when
customers come to visit the kitchen. You only have the oversized pancake flipper left, and you need to use it
quickly to leave all the cooking pancakes happy side up, so that the customers leave feeling happy with their visit.

Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake
flipper needed to leave all pancakes happy side up, or state that there is no way to do it.
"""


def flip_cakes(case_str):
    return ''.join(map(lambda x: '-' if x == '+' else '+', case_str))


def algo(cakes, flip, count=0, states=None):
    index = cakes.find('-')
    if index == -1:
        return count

    states = states or []
    if cakes in states:
        return 'IMPOSSIBLE'

    states.append(cakes)
    index = index if index+flip <= len(cakes) else len(cakes) - flip
    new_cakes = cakes[:index] + flip_cakes(cakes[index:index+flip]) + cakes[index+flip:]
    count += 1
    print cakes, count
    val = algo(new_cakes, flip, count, states)
    if val == 'IMPOSSIBLE' and index < len(cakes) - flip:
        index += 1
        new_cakes = cakes[:index] + flip_cakes(cakes[index:index + flip]) + cakes[index + flip:]
        val = algo(new_cakes, flip, count, states)

    return val


def solve(pancakes, flipper):
    if flipper > len(pancakes):
        return 'IMPOSSIBLE'

    ans = algo(pancakes, flipper)
    return ans


def run(ip, op):
    t = int(ip.readline().replace('\n', ''))
    line = ip.readline().replace('\n', '')
    for i in xrange(t):
        s, n = line.split(' ')
        n = int(n)
        print ''
        print s, ' ', n
        sol = solve(s, n)
        print '%s %s %s' % (s, n, sol)
        op.write('Case #%d: %s\n' % (i+1, sol))

        line = ip.readline().replace('\n', '')

if __name__ == "__main__":
    import sys

    fp = sys.argv[1]
    fpo = fp + '.out'
    rh = open(fp, 'r')
    wh = open(fpo, 'w')
    run(rh, wh)
    rh.close()
    wh.close()

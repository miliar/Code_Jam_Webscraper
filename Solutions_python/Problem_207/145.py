from collections import Counter
import sys

def next_line():
    return input_file.readline().rstrip()

input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    manes = map(int, next_line().split())[1:]
    orig_manes = manes[:]
    manes = [manes[0] - manes[3], manes[2] - manes[5], manes[4] - manes[1]]
    perm = sorted(range(3), key=lambda i: manes[i])
    manes.sort()
    if min(manes) < 0 or manes[2] > manes[0] + manes[1]:
        print "IMPOSSIBLE"
        continue
    #max - t = s1 - t + s2 - t
    #t = s1 + s2 - max
    triplet = manes[0] + manes[1] - manes[2]
    manes = [m-triplet for m in manes]
    s = "RYB" * triplet
    s += "RB" * manes[0] + "YB" * manes[1]
    s = "".join("RYB"[perm["RYB".index(c)]] for c in s)
    #print manes
    colors = "ROYGBV"
    problem = []
    for i in [1, 3, 5]:
        col = colors[i]
        comp = colors[(i+3) % 6]
        if orig_manes[i] and comp in s:
            ind = s.index(comp)
            s = s[:ind] + (comp + col) * orig_manes[i] + s[ind:]
        elif orig_manes[i]:
            problem.append(i)
    if problem:
        if sum([m>0 for m in orig_manes]) > 2:
            print "IMPOSSIBLE"
            continue
        i = problem[0]
        col = colors[i]
        comp = colors[(i+3) % 6]
        s = (comp + col) * orig_manes[i]
    print s
    count = Counter(s)
    assert(all(count[c] == orig_manes[colors.index(c)] for c in colors))

import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    r0 = int(sys.stdin.readline()) - 1
    cards0 = []
    for i in range(4):
        cards0.append(set([int(x) for x in sys.stdin.readline().split()]))

    r1 = int(sys.stdin.readline()) - 1
    cards1 = []
    for i in range(4):
        cards1.append(set([int(x) for x in sys.stdin.readline().split()]))

    r = cards0[r0].intersection(cards1[r1])
    s = ""
    if len(r) == 1:
        s = r.pop()
    elif len(r) > 1:
        s = "Bad Magician!"
    else:
        s = "Volunteer cheated!"

    print "Case #%d: %s" % (t, s)


from sys import stdin
T = int(stdin.readline())
for case in range(1, T + 1):
    args = stdin.readline().split()
    n, s, p = int(args[0]), int(args[1]), int(args[2])
    args = args[3:len(args)]
    count = 0
    for e in args:
        if int(e) < p: continue
        diff = (int(e) - p) / 2 - p
        if diff == -2 and s > 0:
            count += 1
            s -= 1
        elif diff > -2:
            count += 1
    print "Case #%d: %d" %(case, count)

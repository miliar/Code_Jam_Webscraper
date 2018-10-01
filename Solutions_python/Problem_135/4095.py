import sys

f = open(sys.argv[1])
T = int(f.readline())
for t in range(T):
    i = int(f.readline())
    M = [map(int, f.readline().split()) for _ in range(4)]
    j = int(f.readline())
    N = [map(int, f.readline().split()) for _ in range(4)]
    S = set(M [i-1]) & set(N [j-1])
    if (len(S) == 1):
        print "Case #%d:" % (t+1), next(iter(S))
    elif len(S) > 1:
        print "Case #%d:" % (t+1), "Bad magician!"
    else:
        print "Case #%d:" % (t+1), "Volunteer cheated!"

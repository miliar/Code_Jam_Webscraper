import sys
from operator import itemgetter

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    (X, S, R, t, N) = [int(x) for x in f.readline().split()]
    walkways = []
    for i in range(0, N):
        (B, E, w) = [int(x) for x in f.readline().split()]
        walkways.append([B, E, w])
    walkways = sorted(walkways, key=itemgetter(0))
    segments = []
    B = 0
    for walkway in walkways:
        if walkway[0] > B:
            segments.append([B, walkway[0], S])
        segments.append([walkway[0], walkway[1], walkway[2] + S])
        B = walkway[1]
    if X > B:
        segments.append([B, X, S])
    segments = sorted(segments, key=itemgetter(2))
    time = 0
    for segment in segments:
        if t <= 0:
            time += float(segment[1] - segment[0]) / segment[2]
            continue
        needed = float(segment[1] - segment[0]) / (segment[2] + R - S)
        if t >= needed:
            t -= needed
            time += needed
        else:
            first = (segment[2] + R - S) * t
            remaining = (segment[1] - segment[0]) - first
            rest = float(remaining) / segment[2]
            time += t + rest
            t = 0
    print "Case #%d: %0.6f" % (case + 1, time) 

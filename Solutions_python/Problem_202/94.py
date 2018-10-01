#!/usr/local/bin/python
import sys
import heapq

def solve(count):
    N, M = sys.stdin.readline().strip().split()
    N = int(N)
    M = int(M)

    rooks = []
    bishops = []
    for i in range(M):
        c, x, y = sys.stdin.readline().split()
        x = int(x)
        y = int(y)
        if c == 'x':
            rooks.append((x, y))
        if c == '+':
            bishops.append((x, y))
        if c == 'o':
            rooks.append((x, y))
            bishops.append((x, y))

    # Add rooks to fill every row and col
    rookRows = [x for (x, _) in rooks]
    rookCols = [y for (_, y) in rooks]
    r = 1
    c = 1
    addedRooks = []
    while len(addedRooks) + len(rooks) < N:
        while r in rookRows:
            r += 1
        while c in rookCols:
            c += 1
        addedRooks.append((r, c))
        r += 1
        c += 1

    # Add bishops to fill every forwards diagonal
    addedBishops = []

    # All squares on the edges
    def allowed(r):
        return r > 0 and r <= N

    disallowed = []
    disallowed.extend([(1, r-1+c) for (r, c) in bishops if allowed(r-1+c)])
    disallowed.extend([(1, 1-r+c) for (r, c) in bishops if allowed(1-r+c)])
    disallowed.extend([(N, r-N+c) for (r, c) in bishops if allowed(r-N+c)])
    disallowed.extend([(N, N-r+c) for (r, c) in bishops if allowed(N-r+c)])
    disallowed.extend([(r-1+c, 1) for (r, c) in bishops if allowed(r-1+c)])
    disallowed.extend([(1-r+c, 1) for (r, c) in bishops if allowed(1-r+c)])
    disallowed.extend([(r-N+c, N) for (r, c) in bishops if allowed(r-N+c)])
    disallowed.extend([(N-r+c, N) for (r, c) in bishops if allowed(N-r+c)])
    disallowed = set(disallowed)

    edgeSquares = []
    edgeSquares.extend([(x, N) for x in range(1, N+1)])
    edgeSquares.extend([(x, 1) for x in range(1, N+1)])
    edgeSquares.extend([(N, x) for x in range(1, N+1)])
    edgeSquares.extend([(1, x) for x in range(1, N+1)])
    edgeSquares = set(edgeSquares)

    test = disallowed.difference(edgeSquares)
    if (len(test) > 0):
        print "Error"
        return None
    # Gets all edge squares not attacked by bishops and sorts them into categories
    allowed = edgeSquares.difference(disallowed)
    bottom = [(r, c) for (r, c) in allowed if r == 1 and not c == 1 and not c == N]
    top = [(r, c) for (r, c) in allowed if r == N and not c == 1 and not c == N]
    left = [(r, c) for (r, c) in allowed if c == 1 and not r == 1 and not r == N]
    right = [(r, c) for (r, c) in allowed if c == N and not r == 1 and not r == N]
    tlCorner = [(N, 1)] if (N, 1) in allowed else []
    trCorner = [(N, N)] if (N, N) in allowed else []
    blCorner = [(1, 1)] if (1, 1) in allowed else []
    brCorner = [(1, N)] if (1, N) in allowed else []

    topPlacement = set([item for sublist in [top, bottom, tlCorner, trCorner] for item in sublist])
    bottomPlacement = set([item for sublist in [top, bottom, blCorner, brCorner] for item in sublist])
    leftPlacement = set([item for sublist in [left, right, tlCorner, blCorner] for item in sublist])
    rightPlacement = set([item for sublist in [left, right, trCorner, brCorner] for item in sublist])
    for placement in [topPlacement, bottomPlacement, leftPlacement, rightPlacement]:
        if len(placement) > len(addedBishops):
            addedBishops = placement

    addedPieces = []
    earnedPoints = N + len(bishops) + len(addedBishops)

    for (r, c) in addedRooks:
        if (r, c) in addedBishops:
            addedPieces.append(("o", r, c))
            addedBishops.remove((r, c))
        elif (r, c) in bishops:
            addedPieces.append(("o", r, c))
        else:
            addedPieces.append(("x", r, c))
    for (r, c) in addedBishops:
        if (r, c) in rooks:
            addedPieces.append(("o", r, c))
        else:
            addedPieces.append(("+", r, c))

    numAddedModels = len(addedPieces)
    print "Case #{}: {} {}".format(case+1, earnedPoints, numAddedModels)
    for (t, r, c) in addedPieces:
        print t, r, c

cases = int(sys.stdin.readline())
for case in range(cases):
    solve(case)

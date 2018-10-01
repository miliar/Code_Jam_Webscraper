#!/usr/bin/env python
# Benjamin James Wright


def test(i, A, n, m):
    # Now do shit.
    for j in xrange(0, n):
        maximum = max(A[j])
        for k in xrange(0, m):
            # Check its column
            if A[j][k] < maximum:
               B = []
               for l in xrange(0, n):
                   B.append(A[l][k])
               if max(B) > A[j][k]:
                   print("Case #"+str(i+1)+': NO')
                   return
    print("Case #"+str(i+1)+': YES')

n = input()

for i in xrange(0, n):
    x = [int(e) for e in raw_input().split()]
    n = x[0]
    m = x[1]

    A = []
    for j in xrange(0, n):
        A.append([int(e) for e in raw_input().split()])
    test(i, A, n, m)


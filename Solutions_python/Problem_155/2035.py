def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

f = open('A-large.in', 'r')
o = open('output-large', 'w')
n = int(f.readline())
for t in xrange(1,n+1):
    smax, s = f.readline().split()
    A = []
    for char in s:
        A.append(int(char))
    P = prefix_sums(A)
    friendsCounter = 0
    for i in xrange(len(A)):
        if A[i] > 0 and i > (P[i] + friendsCounter):
            friendsCounter += i - (P[i] + friendsCounter)
    o.write('Case #' + str(t) + ': ' + str(friendsCounter) + '\n')

def work1(A,B):
    N = len(A)
    ret = 0
    for i in xrange(N):
        if A[-1] > B[-1]:
            ret = ret + 1
            A = A[:-1]
            B = B[:-1]
        else:
            A = A[1:]
            B = B[:-1]
    return ret

def work2(A,B):
    N = len(A)
    ret = 0
    for i in xrange(N):
        a = A[0]
        A = A[1:]
        flag = 0
        for x in B:
            if x > a:
                B.remove(x)
                flag = 1
                break
        if (not flag):
            B = B[:-1]
            ret = ret + 1
    return ret

with open('D.in', 'r') as f:
    T = int(f.readline())
    for t in xrange(T):
        ret = 'Case #%d: ' % (t+1)
        N = int(f.readline())
        A = [float(x) for x in f.readline().split()]
        B = [float(x) for x in f.readline().split()]
        A.sort()
        B.sort()
        res1 = work1(A,B)
        res2 = work2(A,B)
        ret += '%d %d' % (res1, res2)
        print ret


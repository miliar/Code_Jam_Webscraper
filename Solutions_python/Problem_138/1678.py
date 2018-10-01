import StringIO
import bisect


# input = """4
# 1
# 0.5
# 0.6
# 2
# 0.7 0.2
# 0.8 0.3
# 3
# 0.5 0.1 0.9
# 0.6 0.4 0.3
# 9
# 0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
# 0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458
# """
import random
input = StringIO.StringIO(input)

def main(input):
    T = int(input.readline())
    for i in range(T):
        N = int(input.readline())

        A = map(float, input.readline().split())
        B = map(float, input.readline().split())


        # N = 1000
        # A = [random.random() for k in range(N)]
        # B = [random.random() for k in range(N)]

        A.sort()
        B.sort()

        B_O = B[:]
        A_O = A[:]

        war_score = 0
        for a in A:
            bindex = bisect.bisect_right(B, a)
            if bindex == len(B):
                war_score += 1
                B.pop(0)
            else:
                B.pop(bindex)

        # print war_score,
        print 'Case #%s:' % (i+1),
        A = A_O[:]
        B = B_O[:]
        # import pdb; pdb.set_trace()
        # print A, B
        d_war = N
        for i in xrange(N):
            if all(a > b for a, b in zip(A[i:],B[:N-i])):
                # print 'i', i
                break

            if A[i] < B[N-i-1]:
                # print A[i], B[-i]
                d_war -= 1
            else:
                break

        print d_war, war_score #, A_O, B_O


main(input)

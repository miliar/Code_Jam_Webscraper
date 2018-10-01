T = int(input())
for t in range(T):
    P = input()
    Q = ''
    for i in range(len(P)):
        rest = len(P) - i

        if Q + P[i] * rest <= P:
            Q += P[i]
        else:
            Q += str(int(P[i])-1)
            Q += '9' * (rest-1)
            break
    print('Case #%d:' % (t+1), int(Q))

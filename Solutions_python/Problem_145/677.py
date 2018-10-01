import sys
import itertools

lines = sys.stdin.readlines()

ntests = int(lines[0])





curr = 1
for t in range(1, ntests+1):
    # print
    P, Q = [int(x) for x in lines[curr].split('/')]
    P00 = P
    Q00 = Q
    R = Q-P

    # remove non-2 common factors from P and Q
    P0 = P
    while P0>0:
        if (P0%2)>0:
            break
        P0 /= 2
    # print "P0",P0
    if (Q%P0)==0:
        P /= P0
        Q /= P0

    # Q has to be a factor of 2
    QQ = Q
    possible = True
    while QQ>1:
        quo, rem = divmod(QQ, 2)
        possible = possible and (rem==0)
        QQ = quo

    # reduce P to 1
    PP = P
    QQ = Q
    while PP>1:
        quo, rem = divmod(PP, 2)
        PP = quo
        QQ /= 2
        # print quo, rem, PP, QQ

    # count generations
    G = 0
    QQQ = QQ
    while QQQ>1:
        G += 1
        QQQ = QQQ/2

    # print "final: ", PP, QQ
    # print P, Q, quo, rem, possible, "G:", G

    curr += 1

    # print P00, Q00
    if possible:
        print "Case #"+ str(t) + ": " + str(G)
    else:
        print "Case #"+ str(t) + ": impossible"

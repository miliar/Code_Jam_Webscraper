import sys

T = int(raw_input())

for t in range(1, T+1):
    N = raw_input()
    N_len = len(N)

    if len(N) == 1:
        print 'Case #%d: %s' % (t, N)
        continue

    loop = True
    while loop:
        loop = False
        for i in range(1, N_len):
            if N[i-1] > N[i]:
                loop = True
                N = str(int(N[:i]) - 1) + '9' * (N_len - i)
                #print i, N

    print 'Case #%d: %d' % (t, int(N))

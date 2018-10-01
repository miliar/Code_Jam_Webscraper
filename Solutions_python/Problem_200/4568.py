import sys

T = int(sys.stdin.readline())

for n in range(T):
    N = list(sys.stdin.readline().strip('\n'))
    N = [int(x) for x in N]
    i = 0
    while i < len(N) - 1:
        if N[i] > N[i + 1]:
            if N[i] == 1:
                N = [9] * (len(N) - 1)
                break
            else:
                for j in range(i + 1, len(N)):
                    N[j] = 9
                N[i] -= 1
                if i >= 1:
                    i -= 2
        i += 1
        


    print('Case #%d: %s' % (n + 1, ''.join([str(x) for x in N])))

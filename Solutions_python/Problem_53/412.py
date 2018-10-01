def run(N, K):

    power = [False] * N
    state = [False] * N
    power[0] = True

    for i in range(K):
        for j in range(N):
            if power[j]:
                state[j] = not state[j]
        for j in range(1,N):
            if power[j-1] and state[j-1]:
                power[j] = True
            else:
                power[j] = False


    if power[N-1] and state[N-1]:
        return 'ON'
    return 'OFF'



f = open('A-small-attempt0.in')

for i,l in enumerate(f.readlines()):
    if i > 0 and len(l) > 1:
        N,K = l.split(' ')
        N = int(N)
        K = int(K)
        print 'Case #%s: %s' % (i,run(N,K))

fin = open('A.in', 'r')
fout = open('A.out', 'w')

T = int(fin.readline())
for t in range(1, T+1):
    D, N = map(int, fin.readline().split())
    max_time = -1
    for i in range(N):
        K, S = map(float, fin.readline().split())
        hours = (D - K) / S
        #print K, S, hours
        if hours > max_time:
            max_time = hours
    assert max_time != -1
    ans = D / max_time 
    fout.write('Case #' + str(t) + ': %0.6f\n' % ans)

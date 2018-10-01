T = int(input())
for t in range(1,T+1):
    d,n = [int(s) for s in input().split(' ')]
    ks = []
    for i in range(n):
        ki,si = [int(s) for s in input().split(' ')]
        ks.append((ki,si))

    time = max([(d-k)/s for k,s in ks])
    result = d/time



    print('Case #{}: {}'.format(t,result))

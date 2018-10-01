input = open('C-small-attempt0.in','r')
output = open('C-small.out','w')
out_strs = []

T = int(input.readline())
for t in range(T):
    R, k, N = input.readline().split()
    R = int(R)
    k = int(k)
    N = int(N)
    G = input.readline().split()
    money = 0
    for i in range(R):
        sum = 0
        ngroup = 0
        while ngroup < len(G) and sum+int(G[ngroup]) <= k:
            sum += int(G[ngroup])
            ngroup += 1
        money += sum
        for j in range(ngroup):
            tmp = G[0]
            del G[0]
            G.append(tmp)
    out_strs.append('Case #%d: %d\n'%(t+1,money))
output.writelines(out_strs)

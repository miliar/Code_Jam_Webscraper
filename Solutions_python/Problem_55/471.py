fin = open('in.txt')
fout = open('out.txt','w')

t = int(fin.readline())
for w in range(1,t+1):
    r,k,n = map(int,fin.readline().split())
    n -= 1
    groups = list(map(int,fin.readline().split()))
    i = 0
    tally = 0
    tsum = 0
    j = 0
    while r > 0:
        tally += groups[i]
        #print(tally)
        if i == n:
            i = 0
        else:
            i += 1
        if tally + groups[i] > k or i == j:
            tsum += tally
            tally = 0
            r -= 1
            j = i
    fout.write("Case #{}: {}\n".format(w,tsum))
   
fin.close()
fout.close()

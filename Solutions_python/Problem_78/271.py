
def solve(N, Pd, Pg):
    pd = Pd/100.0
    a = [j for j in [i*pd for i in range(1, N+1)] if j%1==0]
    if len(a)<=0:
        return 'Broken'
    if (Pg==100 or Pg==0) and (Pg != Pd):
        return 'Broken'
    return 'Possible' 
    

input_file = 'A-small-attempt0.in'
output_file = 'result.dat'
fin=open(input_file , 'r')
fout=open(output_file, 'w')

T=int(fin.readline())
for t in range(1, T+1):
    N, Pd, Pg = [int(x) for x in fin.readline().split()]
    ans = 'Case #%d: %s\n'%(t, solve(N, Pd, Pg))
    print(ans)
    fout.write(ans)
fin.close()
fout.close()
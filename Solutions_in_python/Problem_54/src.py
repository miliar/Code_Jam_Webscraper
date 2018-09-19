
def solve(I):
    I.sort()
    xl=[I[i+1]-I[i] for i in range(len(I)-1)]
    xl=[x for x in xl if x>0]
    d = euclids(xl)
   
    if d==1:
        return 0
    
    ans = d-(I[-1]%d)
    if ans==d:
        return 0
    else:
        return ans

def euclid(numA, numB):
    while numB != 0:
        numRem = numA % numB
        numA = numB
        numB = numRem
    return numA

def _euclids(n, N):
    if N==[]:
        return n
    else:
        nn=euclid(n, N[0])
        return _euclids(nn, N[1:])
        

def euclids(N):
    if N==[]:
        return None
    else:
        return _euclids(N[0], N[1:])

#print(euclids([3]))
#print(solve([100000000000000000000000000000000000000000000000000,99999999999999999999999999999999999999999999999999]))

fin = open('B-large.in', 'r')
fout = open('out.txt', 'w')
nc = int(fin.readline().rstrip())
for i in range(1,nc+1):
    I = [int(s) for s in fin.readline().rstrip().split()]
    I = I[1:]
    print(I)
    ans = 'Case #%d: %d\n'%(i, solve(I))
    fout.write(ans)
    print(ans)
    
fin.close()
fout.close()

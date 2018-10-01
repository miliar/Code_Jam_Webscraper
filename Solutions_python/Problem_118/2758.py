import math
def is_square_and_fair(m):#m es int
    rev1 = list(str(m))
    rev1.reverse()
    if '.0' in str(math.sqrt(m)):
        sqofm = int(math.sqrt(m))
    else:
        return False
    rev2 = list(str(sqofm))
    rev2.reverse()
    if str(m) == ''.join(rev1) and str(sqofm) == ''.join(rev2):
        return True
    else:
        return False
    

def solve(infile,outfile):
    ent = open(infile,'r')
    sal = open(outfile,'w')
    T = int(ent.readline())
    for t in range(1,T+1):
        A,B = map(int,ent.readline().split())
        res = 0
        for i in range(A,B+1):
            if is_square_and_fair(i):
                res+=1
        sal.write('Case #'+str(t)+': '+str(res)+'\n')
    
    
def main():
    solve('C-small-attempt0.in','P2.out')

main()
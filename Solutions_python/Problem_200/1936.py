import sys
# print("Case #{}: {} {}".format(i, n + m, n * m))

sys.stdin  = open("inbs.in")
sys.stdout = open("obs.out","w")

def removeZero(s) :
    i = 0
    while s[i]==0 :
        s.remove(0)
    return s



def check(s) :
    for it in range(len(s)-1):
        if(s[it]>s[it+1]) :
            return it
    
    return -1

n = int(input())
for i in range(n) :
    line = list(input())
    line = [int(x) for x in line]
    while(True):
        ind = check(line)
        if(ind == -1):
            break;
        else :
            if(line[ind]>=1) :
                line[ind]=line[ind]-1
                line[ind+1:]=[9 for x in range(len(line)-ind-1)]
            else :
                line[ind]=[9 for x in range(len(line)-ind)]
                #line[ind-1]=line[ind-1]-1
    #print(str(line))
    line = removeZero(line)
    print("Case #",i+1,":",sep='',end=' ')
    for ir in line :
        print(ir,end='')
    print()
   
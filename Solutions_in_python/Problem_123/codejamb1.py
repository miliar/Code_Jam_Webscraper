import sys

x = 0;
n = sys.stdin.readline()
n = int(n)

def cut(n, l):
    ret = []
    for i in range(len(l)):
        if i >= n:
            ret.append(l[i])
    return ret
    
def iter(num, a, mote, cou, r):
    if len(mote) == 0:
        return num
    else:
        if mote[0] < a:
            num = iter(num, a + mote[0], cut(1, mote), cou + 1, r)
        else:
            if cou < r:
                nu1 = iter(num + 1, a + a - 1, mote, cou + 1, r)
            else:
                nu1 = iter(num + 1, a + a - 1, cut(1, mote), cou + 1, r)
            nu2 = iter(num + 1, a, cut(1, mote), cou + 1, r)
            if nu1 < nu2:
                num = nu1
            else:
                num = nu2
    return num


while (x < n):
    x = x + 1 #count
    
    num = 0
	
    ax = sys.stdin.readline().split()
	
    a = int(ax[0])
    r = int(ax[1])

    om = sys.stdin.readline().split()
    mote = []
    

    for i in om:
        mote.append(int(i))
        
    mote.sort()
    
    num = iter(0, a, mote, 0, r)

            
    print("Case #",x,": ",num, sep='')
import sys      

operate_file = True
#operate_file = False

if operate_file:
    sys.stdin = open('in.txt','r')
    sys.stdout = open('out.txt','w')

def F(total, left):
    if total == left + 1:
        return 1
    else:
        return total/2 + F(total/2, (left+1)//2)

def FF(total, left):
    if left > 0:
        return FF(total/2, (left-1)//2)
    else:
        return total
    
def F2(total, p):
    left = 0
    right = total - 1
    mid = 0
    while left <= right:
        mid = (left + right)//2
        res = F(total, total - mid - 1)
        #print total, mid, res, left, right
        if res <= p:
            left = mid + 1
        else:
            right = mid - 1
        #print left, right
    if F(total, total - mid - 1) <= p:
        return mid
    else:
        return mid - 1

def FF2(total, p):
    left = 0
    right = total - 1
    mid = 0
    while left <= right:
        mid = (left + right)//2
        res = FF(total, total - mid - 1)
        #print total, mid, res, left, right
        if res <= p:
            left = mid + 1
        else:
            right = mid - 1
        #print left, right
    if FF(total, total - mid - 1) <= p:
        return mid
    else:
        return mid - 1

T = int(sys.stdin.readline())
for t in range(T):
    NP = sys.stdin.readline().split()
    N = int(NP[0])
    P = int(NP[1])
    total = 1
    for i in range(N):
        total *= 2
    print 'Case #' + str(t+1) + ': ' + str(F2(total, P)) + ' ' + str(FF2(total, P))
    
        



if operate_file:
    sys.stdin.close()
    sys.stdout.close()

import sys

duals = ['G','V','O']

def test(startcol,A,D):
    if len(A[startcol])==0:
        return False # cannot start with this colour
    # Give one more of that type
    A[startcol].append(A[startcol][0])
    # Reduce the dual colours
    for i in range(3):
        while D[i]>0:
            if len(A[i])<2:
                return False
            a = A[i].pop()
            b = A[i].pop()
            A[i].append(a+duals[i]+b)
            D[i] -= 1
            
    # Now count gaps left
    gaps = len(A[startcol])-1
    xi = (startcol+1)%3
    yi = (startcol+2)%3
    x = len(A[xi])
    y = len(A[yi])
    # Order
    if x<y:
        y,x=x,y
        yi,xi=xi,yi
    # Now x >= y
    # Need something in each gap
    # can insert at most x+y things
    #print startcol,gaps,x,y,A,gaps>x+y,x>gaps+y
    if gaps>x+y:
        return False
    # Can place 1 more x than y in each gap
    # can place gaps more x than y in total
    if x>gaps+y:
        return False
    if gaps==0:
        return A[startcol][0][:-1] # Trim off repeated colour
    # Now go through and construct string
    R = []
    for i,s in enumerate(A[startcol]):
        # i is number of gaps filled so far
        R.append(s)
        final = (i==gaps)
        if final:
            break
        lastgap = (i==(gaps-1))
        if lastgap:
            # Alternate all remaining x and y
            assert y+1>=x>=y
            for a in range(x):
                R.append(A[xi].pop())
                x-=1
                if y>0:
                    R.append(A[yi].pop())
                    y-=1
            assert x==y==0 
        else:
            if x>y:
                # Just place a x
                x-=1
                R.append(A[xi].pop())
            else:
                # Place a y
                y-=1
                R.append(A[yi].pop())
    #print x,y,R
    R = ''.join(R)
    assert R[-1]==R[0]
    return R[:-1]

def go(M):
    _, R, O, Y, G, B, V = map(int,M.split())

    YB = G
    RB = V
    RY = O
    dual = 3 # Offset to dual colours
    # Choose a colour to be at the start
    for startcol in range(3):
        A = [ ['R' for i in range(R)],
              ['Y' for i in range(Y)],
              ['B' for i in range(B)] ]
        D = [ YB, RB, RY ]
        result = test(startcol,A,D)
        if result:
            return result
    else:
        # Can have just 1 of a dual colour
        D = [ YB, RB, RY ]
        if R==Y==B==0 and sum(D)==1:
            return D[0]*duals[0]+D[1]*duals[1]+D[2]*duals[2]
        return "IMPOSSIBLE"
                
    
#sys.stdin=open('datab.txt')

T=input()
for t in range(1,T+1):
    M=raw_input()
    print "Case #{}: {}".format(t,go(M))


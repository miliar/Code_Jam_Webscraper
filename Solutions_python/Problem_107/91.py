def process(A,B):
    boxes = 0
    if A[1] == B[1]:
        boxes = min(A[0], B[0])
    A[0]-=boxes
    B[0]-=boxes
    if A[0] == 0:
        del A[0:2]
    if B[0] == 0:
        del B[0:2]
    return boxes


with open('C-small-attempt5.in') as f:
    N = int(f.readline())
    out = file('testD.out','w')
    for case in range(1, N+1):
        
        n,m = map(int, f.readline().split())
        A = map(int, f.readline().split())
        B = map(int, f.readline().split())
        
        highestT= 0
        frontier = [(0,0,A[:],B[:])]
        while True:
            
            cut, total, A, B = frontier.pop()
            while True:
                
                if len(A)==0 or len(B) == 0:
                    break
                boxes = process(A,B)
                if boxes>0:
                    total += boxes
                else:
                    break
                
            if len(A) <= 2 or len(B) <= 2:
                if total>highestT:
                    
                    highestT = total
            
            if len(A)-2 > 0:
                frontier.append((cut+1,total, A[2:], B[:]))
            if len(B)-2 > 0:
                frontier.append((cut+1,total, A[:], B[2:]))
            frontier.sort()
            if len(frontier)==0:
                print highestT
                break
            
        
        
        out.write('Case #%i: %i\n'%(case,highestT))
    out.close()



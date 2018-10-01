t=input()
for _ in range(t):
    (x,r,c)=map(int,raw_input().strip().split())
    if x==1:
        print 'Case #{}: {}'.format(_+1,'GABRIEL')
    elif x==2:
        if (r*c)%2==0:
            print 'Case #{}: {}'.format(_+1,'GABRIEL')
        else:
            print 'Case #{}: {}'.format(_+1,'RICHARD')
    elif x==3:
        if (r*c)%3!=0:
            print 'Case #{}: {}'.format(_+1,'RICHARD')
            continue
        if [r,c] in [[2,3],[3,3],[3,4]] or [c,r] in [[2,3],[3,3],[3,4]]:
            print 'Case #{}: {}'.format(_+1,'GABRIEL')
            
        else:
            print 'Case #{}: {}'.format(_+1,'RICHARD')
    else:
        if [r,c] in [[3,4],[4,4]] or [c,r] in [[3,4],[4,4]]:
            print 'Case #{}: {}'.format(_+1,'GABRIEL')
        else:
            print 'Case #{}: {}'.format(_+1,'RICHARD')
        
        
            

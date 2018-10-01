def solve(t):
    ans1 = int(raw_input());
    pos = []
    for i in range(4):
        line = map(int, raw_input().split(' '))
        if i == ans1 - 1:
            pos = line
    
    ans1 = int(raw_input());
    for i in range(4):
        line = map(int, raw_input().split(' '))
        
        if i == ans1 - 1:
            pos = set(pos).intersection(line)

    if len(pos) == 1:
        print('Case #%d: %d' % ( t  + 1,  pos.pop()))
    elif len(pos)  >  1:
        print('Case #%d: Bad magician!' % ( t + 1) )
    else:
        print('Case #%d: Volunteer cheated!' % ( t + 1) )
    
t = int(raw_input())
for i in range(t):
    solve(i)

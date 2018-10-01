f = open('qp2.in','r')
op = open('qp2.out','w')
numLines = int(f.readline())
for i in range(numLines):
    op.write('Case #')
    op.write(str(i+1))
    op.write(': ')
    line = f.readline().split();
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    x = 0
    y = 0
    for j in range(N):
        total = int(line[j+3])
        if not (p==1 and total==0):
            if total >= 3*p-2:
                x=x+1
            elif total < 3*p-2 and total >= 3*p-4:
                y=y+1
    x = x+min([y,S])
    op.write(str(x))
    op.write('\n')
f.close()
op.close()

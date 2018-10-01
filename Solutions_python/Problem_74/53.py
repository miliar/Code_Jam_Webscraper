

def run():
    f=open("input.in")
    g=open("out.txt",'w')
    num = int(f.readline())
    for i in range(num):
        g.write("Case #%d: " % (i+1))
        steps = f.readline().split()
        seq= int(steps[0])
        ind = 1
        pos=[1,1]
        free = [0,0]
        total=0
        for j in range(seq):
            if (steps[2*j+1]=='O'):
                act = 0
            else:
                act = 1
            newp = int(steps[2*j+2])
            needed = abs(newp-pos[act])
            inc = max([needed-free[act],0])+1
            free[1-act]=free[1-act]+inc
            free[act]=0
            pos[act]=newp
            total=total+inc
        g.write("%d\n"% total)       
    f.close()
    g.close()
    

import sys
f = sys.stdin
if len(sys.argv)>=2:
    fn=sys.argv[1]
    if fn!='_':
        f=open(fn)
output=open('speek.out','w')
t=int(f.readline())
for test in xrange(1,t+1):
    str1="Case #%d: "%(test)
    output.write(str1)
    string=f.readline().strip()
    raj=[]
    for j in string:
        if j=='a':
            raj.append('y')
        elif j=='b':
            raj.append('h')
        elif j=='c':
            raj.append('e')
        elif j=='d':
            raj.append('s')
        elif j=='e':
            raj.append('o')
        elif j=='f':
            raj.append('c')
        elif j=='g':
            raj.append('v')
        elif j=='h':
            raj.append('x')
        elif j=='i':
            raj.append('d')
        elif j=='j':
            raj.append('u')
        elif j=='k':
            raj.append('i')
        elif j=='l':
            raj.append('g')
        elif j=='m':
            raj.append('l')
        elif j=='n':
            raj.append('b')
        elif j=='o':
            raj.append('k')
        elif j=='p':
            raj.append('r')
        elif j=='q':
            raj.append('z')
        elif j=='r':
            raj.append('t')
        elif j=='s':
            raj.append('n')
        elif j=='t':
            raj.append('w')
        elif j=='u':
            raj.append('j')
        elif j=='v':
            raj.append('p')
        elif j=='w':
            raj.append('f')
        elif j=='x':
            raj.append('m')
        elif j=='y':
            raj.append('a')
        elif j=='z':
            raj.append('q')
        elif j==' ':
            raj.append(' ')
    raj=''.join(raj)
    output.write(raj+"\n")
output.close()
               
            

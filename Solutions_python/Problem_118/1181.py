import math
def process_input(infile,T):
    for t in range(T):
        vs = [int(a) for a in infile.readline().split(' ')]
        yield vs


infile = open('C-small-attempt0.in','r')
T = int(infile.readline())
vs = process_input(infile,T)
for t in range(T):
    a,b = vs.next()
    count = 0
    for v in range(int(math.ceil(math.sqrt(a))),int(math.sqrt(b))+1):
        v_str = str(v)
        rev = v_str[::-1]
        if v_str == rev:
            sq = str(v*v)
            if sq == sq[::-1]:
                count += 1
    print 'Case #'+str(t+1)+':',count
        
                
            

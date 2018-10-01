import sys

# input
fin = open("C:/Users/Melissa/My Documents/Python/Inputs/B-large.in", 'r')
fout = open("C:/Users/Melissa/My Documents/Python/Outputs/Magicka-large.txt",'w')

T = int(fin.readline().strip())

for i in xrange(1,T+1):
    inp = fin.readline().strip().split()
    C = int(inp.pop(0))

    combine = []
    for j in xrange(C):
        combine.append(inp.pop(0))

    oppose = []
    D = int(inp.pop(0))
    for k in xrange(D):
        oppose.append(inp.pop(0))

    invoke = []
    N = int(inp.pop(0))
    for char in inp[0]:
        invoke.append(char)
        if len(invoke) < 2:
            continue
        
        else:
            
            for c in combine:
                if ((invoke[-1] == c[0]) and (invoke[-2] == c[1])) or ((invoke[-1] == c[1]) and (invoke[-2] == c[0])):
                    invoke.pop()
                    invoke.pop()
                    invoke.append(c[2])

            for o in oppose:
                if (o[0] in invoke) and (o[1] in invoke):
                    invoke = []

    # output    
    invokestr = str(invoke).replace("'","")                
    print >> fout, "Case #%d: %s" % (i, invokestr)

fin.close()
fout.flush()
fout.close() 
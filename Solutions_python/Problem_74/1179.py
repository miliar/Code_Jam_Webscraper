import sys, re
fp = file(sys.argv[1])

#read params
N = int(fp.next())
 
#read words
#print N

def step(button,place):
    n = button - place
    if n<>0:
        n= n/abs(n)
    return n
    

for i in range(1,N+1):
    inp = [x for x in fp.next().split()]
    #print inp
    d = int(inp[0])
    #print "d is {0}".format(d)
    lp =[]
    lp.append([])
    lp.append([])
    l =[]
    bots= [1,1]
    flag = 'n'
    for j in range(1,2*d+1,2):
        if inp[j]=='O':
            l.append(0)
        else:
            l.append(1)
        lp[l[(j-1)/2]].append(int(inp[j+1]))
    #print lp
    #print l   
    counter = 0
    while len(l)>0:
        #print "l {0}".format(l)
        #print "lp {0}".format(lp)
        #print bots
        if(lp[l[0]][0] == bots[l[0]]):
            del lp[l[0]][0]
            try:
                bots[(l[0]+1)%2] += step(lp[(l[0]+1)%2][0],bots[(l[0]+1)%2])
            except:
                pass
            del l[0]
        else:
            if len(lp[0])>0:
                bots[0] += step(lp[0][0],bots[0])
            if len(lp[1])>0: 
                bots[1] += step(lp[1][0],bots[1])
        counter +=1
    print "Case #{0}: {1}".format(i,counter)
    
fp.close()

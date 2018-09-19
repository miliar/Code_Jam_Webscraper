f = open('q2in.in' , 'r')
amount = int(f.readline())


def parse_result(caseno , result):
    print "Case #" + str(caseno) + ":",str(result)

for i in xrange( 0 , amount):
    cur = f.readline().split(' ')
    cur[len(cur)-1]=cur[len(cur)-1][:-1]
    for t in xrange(0 , len(cur)):
        cur[t]=int(cur[t])
    count = 0
    #print cur
    for a in xrange(0 , cur[0]):
        for b in xrange( 0 , cur[1]):
            if (a & b)>=0 and (a & b)<cur[2]:
                count+=1
        
    parse_result(i+1 , count)
    

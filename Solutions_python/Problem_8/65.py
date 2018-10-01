import sys

primes=[2]

for n in xrange(3,1000):
    for p in primes:
        if(n%p==0):
            break
    else:
        primes.append(n)

def pp(node):
    while node != None:
        print node[0]
        node = node[1]        
        
def mrg(node0, node1):
        if(node1 == None):
            return
        n0 = node0[2]
        n1 = node1[2]
        if(n0 == n1):
            return
        while node0[1] != None:
            node0 = node0[1]
        node0[1] = n1
        while n1 != None:
            n1[2] = n0
            n1 = n1[1]

for case in range(1, int(sys.stdin.readline())+1):
    (A,B,MP) = map(int, sys.stdin.readline().split(' '))
    groups = {}
    nodes = {}
    members = {}
    pg={}
    
    px = [p for p in primes if p >= MP]
    
    for n in xrange(A, B+1):
        node=[n, None, None]
        node[2] = node
        nodes[n] = node
        
    for p in px:
        node=[p, None, None, None]
        node[2] = node
        pg[p] = node

    for n in xrange(A, B+1):
        gid = None
        divs=[]
        for p in px:
            if(n%p > 0):
                continue
            divs.append(p)
        for dd in range(len(divs)):
            r0=pg[divs[dd]][2]
            if(r0[3] == None):
                r0[3] = nodes[n]
            else:
                mrg(r0[3], nodes[n])
            if(dd+1 < len(divs)):
                r1=pg[divs[dd+1]][2]
                mrg(r0, r1)
                mrg(r0[3], r1[3])
        
    count = 0
    for n in xrange(A, B+1):
        if(nodes[n][2] == nodes[n]):
            count += 1
    print "Case #%d: %d" % (case, count)
            
                     
                     
                
        
        

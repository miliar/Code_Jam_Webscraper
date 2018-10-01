import sys

sys.setrecursionlimit(10000)
def getnext(gen, type):
    try:
        l = gen.next().strip("\n")
        return type(l)
    except StopIteration:
        return None

def numSwitches(engines, lst):
    if not lst:
        return 0
    notseen = engines[:]
    for i in range(len(lst)):
        last = lst[i]
        if lst[i] in notseen:
            notseen.remove(lst[i])
        if len(notseen) == 0:
            return 1 + numSwitches(engines, lst[i:])
    return 0

if __name__ == "__main__":
    infi = sys.argv[1]
    reader = open(infi,'r').xreadlines()
    output = open(sys.argv[0]+'-output', 'w')
    N = getnext(reader, int)
    for n in range(N):
        S = getnext(reader, int)
        engines = [getnext(reader, str) for s in range(S)]
        Q = getnext(reader, int)
        queries = [getnext(reader, str) for q in range(Q)]
        #print numSwitches(engines, queries)
        output.write("Case #%d: %d\n" % (n+1, numSwitches(engines, queries)))
        
        
        

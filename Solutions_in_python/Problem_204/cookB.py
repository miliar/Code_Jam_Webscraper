import flownet as flow
import math

def isCompatible(R, Q, r, c, c_):
    lo = math.ceil(Q[r][c] / (1.1 * R[r]))
    hi = math.floor(Q[r][c] / (0.9 * R[r]))

    lo_ = math.ceil(Q[r+1][c_] / (1.1 * R[r+1]))
    hi_ = math.floor(Q[r+1][c_] / (0.9 * R[r+1]))

    

    return (lo <= hi_ and lo_ <= hi)

fileIn = open('B-small-attempt3.in','r')
fileOut = open('out.txt','w')

T = int(fileIn.readline().strip())
for t in range(1, T+1):
    N, P = fileIn.readline().strip().split()
    N, P = int(N), int(P)
    R = [int(_) for _ in fileIn.readline().strip().split()]
    """
    print(str(N)+" "+str(P))
    print(R)
    """
    Q = [0] * N
    for n in range(N):
        Q[n] = [int(_) for _ in fileIn.readline().strip().split()]

    flow_net = flow.FlowNetwork()
    flow_net.addVertex('source', True, False)
    flow_net.addVertex('sink', False, True)
    packages = []
    for r in range(N):
        for c in range(P):
            packages.append((r,c))
    for pt in packages:
        flow_net.addVertex(pt)


    addedEdges = set([])
    for r in range(N-1):
        for c in range(P):
            for c_ in range(P):
                if isCompatible(R, Q, r, c, c_):
                    if not ((r,c),(r+1,c_)) in addedEdges:
                        flow_net.addEdge((r,c), (r+1,c_), 1)
                        addedEdges.add(((r,c),(r+1,c_)))

    for c in range(P):
        flow_net.addEdge('source', (0,c), 1)
        flow_net.addEdge((N-1,c), 'sink', 1)

    m = 0
    if N == 1:
        r = 0
        for c in range(P):
            numbers = [i for i in range(int(10 * Q[r][c] / R[r])) if (.9 * i * R[r] <= Q[r][c] and 1.1 * i * R[r] >= Q[r][c])]
            if len(numbers)>0:
                m += 1
    else:
        m = flow_net.calculateMaxFlow()

    #print("Case #"+str(t)+": "+str(m))
    fileOut.write("Case #"+str(t)+": "+str(m)+"\n")


fileIn.close()
fileOut.close()
        

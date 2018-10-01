import math, sys

###############################################################################
# Helper functions                                                            #
###############################################################################
def dist(a,b):
    res = 0
    for i in range(3):
        res += (b[i]-a[i])*(b[i]-a[i])
    res = math.sqrt(res)
    return res


def parseInput(input):
    case = []    
    # PARSE INPUT

    return case

def handleCase(case):
    res = []    
    # HANDLE CASE

    ave = [0,0,0,0,0,0]
    for fly in case:
        for col in range(len(fly)):
            ave[col] += fly[col]
    for col in range(len(ave)):
        ave[col] /= float(len(case))

    P0 = ave[0:3]
    V = ave[3:]
    dV = dist((0,0,0),V)

    if dV == 0:
        d = dist((0,0,0),P0)
        return (d,0.0)
    
    Vhat = [0,0,0]    
    for i in range(3):
        Vhat[i] = V[i] / dV
    #print Vhat 

    cp = 0
    for i in range(3):
        cp += -P0[i] * Vhat[i]

    if cp < 0:
        d = dist((0,0,0),P0)
        return (d,0.0)

    proj = [0,0,0]
    P2 = [0,0,0]
    for i in range(3):
        proj[i] = cp*Vhat[i]
        P2[i] = P0[i] + proj[i]

    time = dist((0,0,0),proj) / dist((0,0,0),V)
    d = dist((0,0,0),P2)
    return (d,time)
  
    
    
###############################################################################
# Main                                                                        #
###############################################################################

input  = open(sys.argv[1])
output = open(sys.argv[1].replace('in','out'),'w')
#debug  = open(sys.argv[1].replace('in','debug'),'w')

nCases = int(input.readline().strip())

for i in range(nCases):
    nFlies = int(input.readline().strip())
    case = []
    for j in range(nFlies):
        case.append([int(x) for x in input.readline().strip().split()])
    
    d,time = handleCase(case)   

    print "Case #" + str(i+1) + ": " + '%.8f'%d + ' %.8f'%time
    output.write('Case #' + str(i+1) + ": " + '%.8f'%d + ' %.8f'%time + '\r\n')

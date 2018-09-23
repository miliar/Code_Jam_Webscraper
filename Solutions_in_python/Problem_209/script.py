# I run this with python 3.6.1

import numpy as np # used for arrays e.g.; Can be downloaded from www.numpy.org

# I use filenames for input/output
debug=True
#filename = 'sample.in'
#filename = 'A-small-attempt0.in'
filename = 'A-large.in'
outputFilename = filename.replace('in','out')

class Pancake:
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.areaH = 2 * np.pi * self.r * self.h
        self.areaT = np.pi * self.r * self.r
        self.areaTotal = self.areaH + self.areaT
    def __lt__(self, other):
         return self.areaH < other.areaH

def runAlgorithm( N, K, pancakes ):
    pancakes = sorted(pancakes, reverse=True)
    candidates = pancakes[:K]
    rest = pancakes[K:]
    assert len(candidates) + len(rest) == N
    largestRadius = max([ p.r for p in candidates ])
    pancakeWeakest = pancakes[K-1]
    restWithLargeRadius = [p for p in rest if p.r > largestRadius]
    if restWithLargeRadius:
        bestOfRest = restWithLargeRadius[0]
        for p in restWithLargeRadius[1:]:
            if p.areaTotal > bestOfRest.areaTotal:
                bestOfRest = p
        if bestOfRest.areaTotal > pancakeWeakest.areaH + largestRadius*largestRadius*np.pi:
            return sum([ p.areaH for p in candidates[:-1] ]) + bestOfRest.areaTotal
    return sum([ p.areaH for p in candidates ]) + largestRadius*largestRadius*np.pi

# handle file input/output and call above algorithm for each case
open( outputFilename, 'w' ) # clear output file
with open(filename, 'r') as f:
    caseCount = int( f.readline().strip() )
    for i in range( 1, caseCount+1 ):
        print('i:', i) # show progress
        data = f.readline().strip().split(' ')
        N = int( data[0] ) # total
        K = int( data[1] ) # demanded
        pancakes = []
        for h in range(N):
            data = f.readline().strip().split(' ')
            R = ( int( data[0] ) )
            H = ( int( data[1] ) )
            pancakes.append( Pancake( R, H ) )
        result = runAlgorithm( N, K, pancakes )
        with open( outputFilename, 'a' ) as f2:
            outputLine = 'Case #{}: '.format(i) + '{:.9f}'.format(result)
            if debug:
                print(outputLine)
            f2.write( outputLine + '\n')
            

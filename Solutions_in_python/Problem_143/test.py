from copy import deepcopy
from itertools import permutations
import cProfile

maxLen = 0
def reader(inpC):

    lines = inpC.readlines(1)

    return list(map(int, lines[0].split()))

def binLen(num):
    return len(bin(num)) - 2
def solver(data):
    maxA, maxB, K = data
    c = 0
    for a in range(maxA):
        for b in range(maxB):
            if a & b < K:
                c += 1

    return c
                
    bA, bB, bK = binLen(maxA), binLen(maxB), binLen(K)
    binMinAB = min(bA, bB)
    
    biNum = int("1" * maxN, 2)
    

    return 3



if __name__ == '__main__':
    from GCJ import GCJ
    #cProfile.run('GCJ(reader, solver, "./", "a").run()')
    GCJ(reader, solver, "./", "a", []).run()



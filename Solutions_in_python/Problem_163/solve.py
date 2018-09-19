#!/usr/bin/env python3
import sys
import logging
import itertools

def solve(R,C,N):
    def score(layout):
        # layout = list of 1-d positions with occupants
        # adjacent if:
            # +/- 1 is occupied and on same row
            # +/- r is occupied
        total = 0
        for r in range(R):
            for c in range(C):
                if (r*C)+c in layout:
                    # right wall
                    if c < C-1:
                        if ((r*C)+c+1) in layout:
                            total += 1
                    # bottom wall
                    if r < R-1:
                        if (((r+1)*C)+c) in layout:
                            total += 1
        return total

    
    #logging.debug([(layout,score(layout)) for layout in itertools.combinations(range(R*C),N)])
    return min([score(layout) for layout in itertools.combinations(range(R*C),N)])

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    cases = sys.argv[1]
    out = cases.replace(".in",".out")
    with open(cases,"r") as i:
        with open(out,"w") as o:
            T = int(i.readline())
            for t in range(T):
                problem = [ int(s) for s in i.readline().split()]
                answer = solve(problem[0],problem[1],problem[2])
                o.write("Case #{}: {}\n".format(t+1, answer))

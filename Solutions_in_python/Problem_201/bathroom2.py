from heapq import *

class Gap:
    def __init__(self, l, r):
        self.r = r
        self.l = l
    def __lt__(g1, g2):
        return (g1.r-g1.l) > (g2.r-g2.l)
    def __le__(g1, g2):
        return (g1.r-g1.l) >= (g2.r-g2.l)

def bathroom(filename):
    infile = open(filename, "r+")
    outfile = open("bathroom_out.txt", "w+")
    inlines = infile.readlines()
    for m in range(1, len(inlines)):
        line = inlines[m].split(" ")
        N = int(line[0])
        K = int(line[1])
        gaps = [Gap(0, N+1)]
        pos = [0, N+1]
        last = -1
        k = 0
        while k < K-1:
            g = heappop(gaps)
            last = (g.l+g.r)/2
            pos.append(last)
            gl = Gap(g.l, last)
            gr = Gap(last, g.r)
            heappush(gaps, gl)
            heappush(gaps, gr)
            k += 1
        lastg = heappop(gaps)
        if m == 1:
            print(gaps[0].l, gaps[0].r)
            print(lastg.l, lastg.r)
            print(pos)
        left = (lastg.l+lastg.r)/2-lastg.l-1
        right = lastg.r-(lastg.l+lastg.r)/2-1
        minLR = min(left, right)
        maxLR = max(left, right)
        outfile.write("Case #" + str(m) + ": " + str(maxLR) + " " + str(minLR) + "\n")
    infile.close()
    outfile.close()

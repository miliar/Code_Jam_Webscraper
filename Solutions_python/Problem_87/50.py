from collections import defaultdict
import os
import sys

with open("in.txt") as f:
    with open("out.txt", "w") as out:
        for case in range(1, int(f.readline()) + 1):
            out.write("Case #%s: " % case)
            len, s, r, t, n = (float(v) for v in f.readline().split())
            wws = []
            for i in range(0, int(n)):
                b, e, ws = (float(v) for v in f.readline().split())
                wws.append((ws, (e - b)))
                
            wws.append((0, len - (sum(v[1] for v in wws))))
            wws.sort()
            result = 0.0
            for w in wws:
                if t == 0:
                    result += w[1] / (w[0] + s)
                elif t > w[1] / (w[0] + r):
                    result += w[1] / (w[0] + r)
                    t -= w[1] / (w[0] + r)
                else:
                    fast_time = w[1] / (w[0] + r)
                    per_done = t / fast_time
                    result += t
                    result += w[1] * (1.0 - per_done) / (w[0] + s)
                    t = 0
            out.write("%.9f" % result)
                    
            out.write("\n")
"""
ted1Ba.py
Google Code Jam 2017
Round 1B Problem a
"""

from sys import stdin

def _main(case_num):
    D, N = map(int, stdin.readline().strip().split())
    D = float(D)

    tmax = -1
    for n in range(N):
        K, S = map(float, stdin.readline().strip().split())
        t = (D - K) / S
        if t > tmax or tmax == -1:
            tmax = t
    speed = D / tmax

    return "Case #%d: %f" % (case_num, speed)


# get input and run main on each line
T = int(stdin.readline().strip())
lines = []
for t in range(1,T+1):
    lines.append(_main(t))
# write the output to file
with open('ted1Ba.out', 'w') as outfile:
    outfile.write("\n".join(lines))

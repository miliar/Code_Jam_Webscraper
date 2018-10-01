"""
Google Code Jam 2010
Qualification Round
Challenge: A. Snapper Chain

By Marcel Rodrigues

Code for Python 2.x
"""

filename = "A-large"

inpath = filename + ".in"
outpath = filename + ".out"

infile = open(inpath, "r")
outfile = open(outpath, "w")

def light(N, K):
    p = 1 << N
    return K % p == p - 1

ncases = int(infile.readline().rstrip())

for case in range(ncases):
    N, K = infile.readline().rstrip().split()
    N, K = int(N), int(K)
    state = "ON" if light(N, K) else "OFF"
    outfile.write("Case #%d: %s\n" % (case + 1, state))

infile.close()
outfile.close()

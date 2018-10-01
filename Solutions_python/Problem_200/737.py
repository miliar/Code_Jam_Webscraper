from __future__ import print_function
import sys

name = sys.argv[1]
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
T = int(input())

for testCase in range(1, T + 1):
    n = int(input().strip())
    tidy = False
    while not tidy:
        eprint(n)
        sn = str(n)
        tidy = True
        if len(sn) <= 1:
            break
        for pos in range(len(sn) - 2, -1, -1):
            eprint("pos", pos, len(sn), int(sn[pos]), int(sn[pos+1]))
            if int(sn[pos]) > int(sn[pos+1]):
                tidy = False
                eprint("removing", int(sn[pos+1:])+1)
                n = n - int(sn[pos+1:]) - 1
                break
    print("Case #" + str(testCase) + ": " + ("%d" % n))

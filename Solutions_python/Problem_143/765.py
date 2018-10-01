#-------------------------------------------------------------------------------
# Name:        module1
# Author:      root
# Created:     03/05/2014
#-------------------------------------------------------------------------------
import sys
fin = open("B-small-attempt0.in")
fout = open("lotteryoutput.txt","w")
T = int(fin.readline())
for f in range (T):
    ABK = fin.readline().split()
    A = int(ABK[0])
    B = int(ABK[1])
    K = int(ABK[2])
    winners = 0
    for a in range(A):
        for b in range(B):
            if a & b < K and a&b >= 0:
                winners+= 1
    fout.write("Case #" + str(f+1) + ": " + str(winners) + "\n")
fout.close()
fin.close()


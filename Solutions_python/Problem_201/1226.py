from sys import stdin, stdout
import math

t = int(raw_input())
for cur in range(1,t+1):
    n, k  = map(int, raw_input().split())
    log2k = int(math.log(k, 2))
    rem   = n - k
    pot   = pow(2, log2k+1)
    
    minV = maxV = int(rem / pot)
    if (rem % pot >= pot/2):
        maxV = maxV + 1
    stdout.write("Case #" + str(cur) + ": " + str(maxV) + " " + str(minV) + "\n")
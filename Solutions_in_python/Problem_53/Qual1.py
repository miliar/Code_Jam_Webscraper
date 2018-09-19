#Tested locally with Python 2.6.2 on OS X 10.6.3
import math

input = open('A-large.in','r')
output = open('A-large.out','w')
T = int(input.next())

for i in range(0,T):
    numsin = input.next().split(' ')
    N = int(numsin[0])
    K = int(numsin[1])

    mask = (1 << N) - 1

    if (mask & K) == mask:
        output.write("Case #"+str(i+1)+": ON\n")
    else:
        output.write("Case #"+str(i+1)+": OFF\n")

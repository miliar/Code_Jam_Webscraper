input = open("A-large.in")
import math

T = int(input.readline())

for t in range(T):
    line = input.readline().split("/")
    P = int(line[0])
    Q = int(line[1])
    K = math.pow(2,40)*P/Q
    if (K == int(K)):
        print("Case #"+str(t+1)+": "+str(40-int(math.log(K, 2))))
    else:
        print("Case #"+str(t+1)+": impossible")

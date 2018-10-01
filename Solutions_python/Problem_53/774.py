import sys
import math

inp = open("A-large.in")
outp = open("output.txt", 'w')

cases = int(inp.readline())

for i in range(0, cases):
    parameters = inp.readline().rstrip().split(" ")
    
    outp.write("Case #" + str(i+1) + ": ")
    if (((int(parameters[1]) + 1) % (math.pow(2, int(parameters[0])))) == 0):
        outp.write("ON")
    else:
        outp.write("OFF")
    
    if (i < (cases - 1)):
        outp.write("\n")
    
inp.close()
outp.close()
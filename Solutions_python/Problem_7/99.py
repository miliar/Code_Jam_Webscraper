import time
import math

filename = "A-small-attempt0.in"

file = open(filename)
out=open(filename.replace("in","out"), 'w')

line_num = 0
cases = 0

line = file.readline()
cases = eval(line)
print 'Number of cases', cases

for case in range(cases):  
    line = file.readline().strip().split()
    
    n = eval(line[0])
    A = eval(line[1])
    B = eval(line[2])
    C = eval(line[3])
    D = eval(line[4])
    x0 = eval(line[5])
    y0 = eval(line[6])
    M = eval(line[7])
  
    X = x0
    Y = y0
    
    xs = []
    xs.append(x0)
    ys = []
    ys.append(y0)
    
    print X, Y
    for i in range(n-1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        print X, Y
        xs.append(X)
        ys.append(Y)

  
    #for x,y in zip(xs,ys):
    middlesx=[]
    middlesy=[]
     
    i=0

    while i < len(xs):
        j = i + 1
        while j > i and j < len(xs):
            k = j + 1
            while k > j and k < len(xs):
                x = 1. *(xs[i] + xs[j] + xs[k])  / 3.   
                y = 1. *(ys[i] + ys[j] + ys[k]) / 3.
                middlesx.append(x)
                middlesy.append(y)
                k += 1
            j += 1
        i += 1
    
    count = 0
    #check for int
    for x,y in zip(middlesx,middlesy):
        if x % 1 == 0 and y % 1 == 0:
            count += 1
  
    s ="Case #" + str(1+case) + ": " + str(count)
    print s
    out.write(s + '\n')

    line_num += 1

file.close()
out.close()
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [s for s in raw_input().split(" ")]  # read a list of string, int
    #greedy Algorithm
    flipperSize = int(m)
    boolArr = [True if c=='+' else False for c in n]
    count=0
    for j in range(len(boolArr)-flipperSize+1):
        if not boolArr[j]:
            count+=1
            for k in range(flipperSize):
                boolArr[k+j]= not boolArr[k+j]
    if False in boolArr:
        print "Case #" +str(i)+": " + "IMPOSSIBLE"
    else:
        print "Case #" +str(i)+": " + str(count)
  # check out .format's specification for more formatting options

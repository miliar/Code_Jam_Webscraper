import sys

filename = sys.argv[1]
print "Using file", filename
inputf = open(filename, 'r')
outputname = filename[:-2] + "out"
outputf = open(outputname, 'w')

cases = int(inputf.readline())
print cases, "test cases"
for case in range(1, cases + 1):
    outputf.write("Case #" + str(case) + ": ")
    print "Case", case
    
    n = int(inputf.readline())
    lines = []
    for i in range(n):
        max = 0
        el = inputf.readline()
        for e in range(n):
            if el[e] == "1":
                max = e
        lines.append(max)
    print lines
    
    swaps = 0
    
    for i in range(n):
        cur = i
        while lines[cur] > i:
            cur += 1
        if cur != i:
            li = lines.pop(cur)
            lines.insert(i, li)
            swaps += cur - i
        print lines
    print "swaps: ", swaps
    
    outputf.write(str(swaps) + "\n")
    
    
inputf.close()
outputf.close()

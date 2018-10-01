import sys

t = int(sys.stdin.readline())

case = 1

for line in sys.stdin:
    sout = "Case #" + str(case) + ": " 
    line = line.split(" ")
    n = int (line[0])
    s = int (line[1])
    p = int (line[2])
    c = 0
    for i in range(3,len(line)):
        ti = int(line[i])
        if p == 0:
            c = c+1
        else:
            if p == 1 and ti > 0:
                c = c+1
            else:
                ti = max(0,ti-max(0,p-2)*3)
                if ti >= 4:
                    c = c+1
                else: 
                    if (ti >= 2 and (s>0)):
                        s = s-1
                        c = c+1
    sout = sout + str(c)
    print(sout)
    case = case + 1

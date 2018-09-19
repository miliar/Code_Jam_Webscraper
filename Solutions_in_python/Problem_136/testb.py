import sys, copy;

c, f, x = 0, 0, 0

def solve():
    r1 = 2;
    e1 = x / r1;
    r2 = r1 + f;
    t = c / r1;
    e2 = t + x / r2;
    while ( e2 < e1 ):
        r1 = r2;
        e1 = e2;
        r2 = r1 + f;
        t = t + c / r1;
        e2 = t + x / r2;
    return e1;    

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print inputFile, outputFile
file = open(outputFile, "w")

with open(inputFile, 'r') as cin:
    t = int(cin.readline())
    print t
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        c, f, x = map(float, cin.readline().split())
        file.write(str(solve()) + "\n")
file.close()            









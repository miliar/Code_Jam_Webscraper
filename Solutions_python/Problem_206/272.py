import sys

inputName = "A-input.txt"

if (len(sys.argv)>1):
    inputName = sys.argv[1]

inFile = open(inputName, "rt")
outFile = open(inputName+".out", "wt")

T = int(inFile.readline())
for testCase in range(1, T + 1):
    outFile.write("Case #"+str(testCase)+": ")
    line = inFile.readline().strip().split()
    D = int(line[0])
    N = int(line[1])
    max_time = 0.0
    for j in range (N):
        line = inFile.readline().strip().split()
        pos = int(line[0])
        speed = int(line[1])
        if (max_time < float(D-pos)/speed):
            max_time = float(D-pos)/speed
        

    outFile.write(str(float(D)/max_time)+"\n")

inFile.close()
outFile.close()



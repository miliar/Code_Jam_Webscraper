infile = open("A-large.in","r")
outfile = open("A-large.out","w")

T = int(infile.readline())

for case in range(T):
    solution = 0
    maxShy, shynesses = infile.readline().split()
    maxShy = int(maxShy)
    shynesses = list(shynesses)
    total = 0
    for shyness in range(maxShy+1):
        while total < shyness:
            solution += 1
            total += 1
        total += int(shynesses[shyness])
    outfile.write("Case #" + str(case+1) + ": " + str(solution) + "\n")

infile.close()
outfile.close()

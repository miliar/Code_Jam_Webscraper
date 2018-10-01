input = open("input.txt").readlines()
output = open("output.txt", "w")
for i in range(len(input)):
    if input[i][-1] == '\n':
        input[i] = input[i][:-1]

nOfCases = int(input[0])
cursor = 1

for casecount in range(nOfCases):
    n = int(input[cursor])
    cursor += 1
    
    a = input[cursor].split()
    b = input[cursor+1].split()
    cursor += 2

    a = [int(i) for i in a]
    b = [int(i) for i in b]

    a.sort()
    b.sort()
    
    sum = 0
    for j in range(n):
        sum += a[j]*b[n-1-j]
    
    
    print >> output, "Case #" + str(casecount+1) + ": " + str(sum)
    print "Case #" + str(casecount+1) + ": " + str(sum)

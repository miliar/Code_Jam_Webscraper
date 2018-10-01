voc = ['a', 'e', 'i', 'o', 'u']
def solve(name, n):
    solution = 0
    count = 0
    start = 0
    pos = []
    for i in range(0, len(name)):
        c = name[i]
        if c not in voc:
            if count == 0:
                start = i
            count += 1
            if count == n:
                pos.append([start, i])
                count -= 1
                start += 1
        else:
            count = 0
    for i in range(0, len(name) - n + 1):
        for j in range(i + n - 1, len(name)):
            for couple in pos:
                if i <= couple[0] and j >= couple[1]:
                    #print(str(i) + ' ' + str(j) + ' ' + str(couple[0]) + ' ' + str(couple[1]))
                    solution += 1
                    break
                    
    return str(solution)

fileIn = open('A-small-attempt0.in')
fileOut = open('A-small-attempt0.out', 'w')
numcases = int(fileIn.readline())
for casenum in range(1,numcases+1):
    line = fileIn.readline()
    name = list(line.split()[0])
    n = int(line.split()[1])
    if n == 0:
        fileOut.write('Case #' + repr(casenum) + ': 0\n')
    else:
        s = solve(name, n)
        fileOut.write('Case #' + repr(casenum) + ': ' + s + '\n')
        #print('Case #' + repr(casenum) + ': ' + s)
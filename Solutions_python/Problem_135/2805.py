def parseCase(case):
    lst = case.split('\n')
    l1 = lst[int(lst[0])].split(' ')
    l2 = lst[int(lst[5])+5].split(' ')

    out = [i for i in l1 if i in l2]

    if len(out) == 0:
        return 'Volunteer cheated!'
    if len(out) > 1:
        return 'Bad magician!'
    return out[0]






fname = raw_input('filename: ')
outname = fname.replace('.in','') + '.out'
out = open(outname,'w')

T = -1
f = open(fname, 'r')


caseNum = 1
with open(fname,'r') as f:
    currCase = ''
    currCount = 0
    for line in f:
        if T == -1:
            T = line
            continue
        if currCount == 10:
            out.write('Case #' + str(caseNum) + ': ' + parseCase(currCase) + '\n')
            currCase = ''
            currCount = 0
            caseNum += 1

        currCase = currCase + line
        currCount += 1

    if currCount == 10:
        out.write('Case #' + str(caseNum) + ': ' + parseCase(currCase) + '\n')
        currCase = ''
        currCount = 0
        caseNum += 1
            
f.close()
out.close()


print '\t', outname, ':'
g = open(outname,'r')
print g.read()
g.close()

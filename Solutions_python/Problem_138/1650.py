"""
python solution for minesweeper
author: _where
"""
outfile = open('output.out', 'w')
def initial():
    infile = open('input.in')
    testCases = int(infile.readline())
    for p in range(testCases):
        outfile.write('Case #%s: ' % (p+1),)
        infile.readline()
        naomi = [float(x) for x in infile.readline().rstrip().split(' ')]
        ken = [float(x) for x in infile.readline().rstrip().split(' ')]
        if (p+1 != testCases): analyze(naomi, ken, False)
        else: analyze(naomi, ken, True)
    outfile.close()
    infile.close()

def analyze(naomi, ken, boo):
    outfile.write('%s %s' % (deceitwar(naomi, ken), war(naomi, ken)))
    if not boo: outfile.write('\n')

def war(naomi, ken):
    tempNao = naomi[:]
    tempKen = ken[:]
    value = 0
    while True:
        start = min(tempNao)
        tempKen.sort()
        seen = False
        for i in range(len(tempKen)):
            if tempKen[i] > start:
                tempKen.remove(tempKen[i])
                tempNao.remove(start)
                seen = True
                break
        if not seen:
            tempKen.remove(min(tempKen))
            tempNao.remove(start)
            value += 1
        if len(tempKen) == 0:
            break
    return value

def deceitwar(naomi, ken):
    tempNao = naomi[:]
    tempKen = ken[:]
    value = 0
    while True:
        start = max(tempKen)
        tempNao.sort()
        seen = False
        for i in range(len(tempNao)):
            if tempNao[i] > start:
                tempNao.remove(tempNao[i])
                tempKen.remove(start)
                value += 1
                seen = True
                break
        if not seen:
            tempNao.remove(min(tempNao))
            tempKen.remove(start)
        if len(tempKen) == 0:
            break
    return value
if __name__ == '__main__':
    initial();
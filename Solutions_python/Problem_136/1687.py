"""
python solution for cookieclicker
author: _where
"""
outfile = open('output.out', 'w')
def initial():
    infile = open('input.in')
    testCases = int(infile.readline())
    for p in range(testCases):
        outfile.write('Case #%s: ' % (p+1),)
        mainArray = ([float(x) for x in infile.readline().rstrip().split(' ')])
        if (p+1 != testCases): analyze(mainArray[0], mainArray[1], mainArray[2], False)
        else: analyze(mainArray[0], mainArray[1], mainArray[2], True)
    outfile.close()
    infile.close()

def analyze(one, two, max, boo):
    first = goIn(one, two, max, 0)
    second = goIn(one, two, max, 1)
    if first < second: 
        outfile.write(format(first, '.7f'))
        if not boo: outfile.write('\n')
    else:
        solutions = []
        solutions.append(second)
        num = 1
        found = False
        global minimum 
        while True:
            num += 1 
            solutions.append(goIn(one, two, max, num))
            for k in range(1, len(solutions)):
                if solutions[k-1] < solutions[k]: 
                    outfile.write(format(solutions[k-1], '.7f'))
                    if not boo: outfile.write('\n')
                    found = True
                    break
            if found:
                 break

def goIn(one, two, max, k):
    currentRate = 2
    time = 0
    now = 0
    while True:
        if (now < k): time += one / currentRate
        else: 
            time += max / currentRate
            break
        currentRate += two
        now += 1
    return time
    
if __name__ == '__main__':
    initial();
    #goIn(30.0, 1.0, 2.0, 1)
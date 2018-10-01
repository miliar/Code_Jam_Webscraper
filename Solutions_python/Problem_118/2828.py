import math

def process(fname):
    lines = readfile(fname + '.in')
    fout = open(fname + '.out', 'w')
    run(lines, fout)

def readfile(fname):
    fin = open(fname)
    rawlines = fin.readlines()
    lines = []
    for rawline in rawlines:
        lines.append(rawline.strip('\n'))
    return lines

def run(lines, fout):
    t = int(lines[0])
    for i in range(t):
        fout.write("Case #" + str(i+1) + ": ")
        lsplit = lines[i+1].split(' ')
        start = lsplit[0]
        end = lsplit[1]
        fout.write(str(fairsquare(start, end)) + '\n')

def ispalindrome(n):
    s = str(n)
    m = int(s[::-1])
    return(m == n)

def fairsquare(m, n):
    low = math.ceil(math.sqrt(float(m)))
    high = math.floor(math.sqrt(float(n)))
    count = 0
    for i in range(low, high + 1):
        if ispalindrome(i):
            if ispalindrome(pow(i,2)):
                count += 1
    return count

def problem(inPath, outDir = ""):
    def solve(inPath, processor, outDir = ""):
        from multiprocessing import Pool
        from os import path

        inf = open(inPath, 'rU')
        stem = path.basename(inPath)
        name, extension = path.splitext(stem)
        outName = name + ".out"
        outPath = path.join(outDir, outName)
        outf = open(outPath, 'w')

        inf.readline() #discard the line which tells us how many lines of input there are
        pool = Pool()
        outputs = pool.map(processor, (line.strip() for line in inf))
        for i, result in enumerate(outputs, 1):
            string = "Case #%s: %s" % (i, result)
            if i > 1:
                outf.write("\n")
            outf.write(string)

    solve(inPath, processor, outDir)

def processor(string):
    return answer(string)

def isTidy(n):
    s = str(n)
    return s == "".join(sorted(s))

def answer(string):    
    firstUntidy = None
    for i in range(len(string) - 1):
        if string[i] > string[i + 1]:
            firstUntidy = i
            break

    if firstUntidy is None:
        return string

    lastAccepted = None
    char = ""
    for j in range(firstUntidy, -1, -1):
        old = string[j]
        new = str(int(old) - 1)
        if new == "0":
            continue
        else:
            if j > 0 and string[j - 1] > new:
                continue
            lastAccepted = j
            char = new
            break

    if lastAccepted is None:
        return "".ljust(len(string) - 1, "9")

    return (string[:lastAccepted] + char).ljust(len(string), "9")
    
        
##    if firstUntidy == 0:
##        return "".ljust(len(string) - 1, "9")
##    else:
##        return string[:firstUntidy].ljust(len(string), "9")
    
def naive(string):
    n = int(string)
    for i in range(n, 0, -1):
        if isTidy(i):
            return str(i)
    return 1

def test(inPath):
    inf = open(inPath, 'rU')
    inf.readline()
    for i, line in enumerate(inf):
        s = line.strip()
        calced = answer(s)
        tested = naive(s)
        if calced != tested:
            print(i, s, calced, tested)

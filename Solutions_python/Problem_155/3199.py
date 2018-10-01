def calculate(smax, sk):
    if smax == 0:
        return 0

    total = 0
    current = 0
    add = 0
    for i in range(0, smax+1):
        total = total + int(sk[i])
        if current >= i:
            current = current + int(sk[i])
        elif sk[i] > 0:
            temp = i - current
            add = add + temp
            current = current + temp + int(sk[i])
    
    return add

def main():
    inFile = "A-large.in"
    outFile = "A-large.out"

    f = open(outFile,'w')
    with open(inFile) as inputFile:
        for i, line in enumerate(inputFile):
            if i > 0:
                s = [n for n in str.split(line)]
                #print "Case #" + str(i) + ": " + str(calculate(int(s[0]), s[1])) + "\n"
                f.write("Case #" + str(i) + ": " + str(calculate(int(s[0]), s[1])) + "\n")
    f.close()

if __name__ == '__main__':
    main()
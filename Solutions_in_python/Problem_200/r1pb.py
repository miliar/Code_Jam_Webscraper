import sys



def main(inputLines):
    case = 0
    lineArr = inputLines.split()
    n = int(lineArr[0])
    for i in range(n):
        curNum = int(lineArr[i+1])
        curNumString = list(lineArr[i+1])
        outputString = "Case #" + str(i+1) + ": "
        if (curNum < 10):
            print outputString + curNumString[0]
            continue
        x = 0
        while (x+1 < len(curNumString)):
            if (curNumString[x+1] < curNumString[x]):
                curNumString[x] =str( int(curNumString[x]) - 1);
                for ind in range(x+1, len(curNumString)):
                    curNumString[ind] = '9'
                if (x > 0 and curNumString[x-1] > '0'):
                    x-=1
                    continue
            x+=1
        print outputString + str(int(''.join(curNumString)))
    return













if __name__ == '__main__':
    if (sys.argv.len() < 2):
        print "Not enough args"
        exit(-1)
    main(sys.argv[1])
    exit(0)
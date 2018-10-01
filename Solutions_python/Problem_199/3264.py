import sys
import optparse

debug = False


def setData(data, numList):
    ret = ''
    strData = str(data)

    for i in range(len(strData)):
        if debug:
            print('[+] numList ' + str(numList))
        cmp = strData[i]
        if cmp in numList:
            ret = cmp
            numList.remove(cmp)
    return ret


def flip(S, K, index):
    for i in range(K):
        if S[index + i] == '+':
            S[index + i] = '-'
        else:
            S[index + i] = '+'
    if debug:        
        print(S)


def moveHappy(S, K, index):
    result = 0
    for i in range(len(S) - index):
        if S[index + i] == '+':
            result += 1
        else:
            break
    if debug:
        print(index + result)
    return index + result

def isAllHappy(S):
    for i in range(len(S)):
        if S[i] == '-':
            return False
    return True
def solve(data):
    if debug:
        print('[+] input data %s %s' % (data[0], data[1]))

    flipCount = 0

    S = []
    for i in range(len(data[0])):
        S.append(data[0][i])
    K = int(data[1])

    index = 0

    index = moveHappy(S, K, index)

    while index + K <= len(S):
        flip(S, K, index)
        flipCount += 1
        index = moveHappy(S, K, index)

    if not isAllHappy(S):
        flipCount = 'IMPOSSIBLE'
    return flipCount


def readData(infile):
    S, K = map(str, infile.readline().strip().split())
    return S, K


def howto():
    usage = ' -i <input file> [-o <output file>]'
    parser = optparse.OptionParser(sys.argv[0] + usage)
    parser.add_option(
        '-i', dest='infile', type='string', help='specify infile name')
    parser.add_option(
        '-o', dest='outfile', type='string', help='specify outfile name')
    (options, args) = parser.parse_args()
    if options.infile is None:
        print(parser.usage)
    return options.infile, options.outfile

if __name__ == '__main__':
    #infile, outfile = howto()
    infile = "a_input.txt"
    outfile = "a_out.txt"
    if infile is None:
        exit()

    infile = open(infile, 'r')
    if outfile is not None:
        outfile = open(outfile, 'w')

    T = int(infile.readline().strip())
    for caseN in range(1, T + 1):
        data = readData(infile)
        result = solve(data)
        resultForm = 'Case #%i: %s\n' % (caseN, result)

        if outfile:
            outfile.write(resultForm)
        else:
            print(resultForm)

    infile.close()
    if outfile is not None:
        outfile.close()

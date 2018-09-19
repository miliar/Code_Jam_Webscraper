import sys
import getopt

def readMatrix(file):
    res = []
    for i in range(4):
        line = file.readline().split()
        res.append(set(line))
    return res
    
def main(argv=sys.argv):
    file = open(sys.argv[1], 'r')
    lines = int(file.readline())
    for prob in range(lines):
        firstRow = int(file.readline())
        firstMatrix = readMatrix(file)
        secondRow = int(file.readline())
        secondMatrix = readMatrix(file)
        diff = firstMatrix[firstRow-1].intersection(secondMatrix[secondRow-1])
        if len(diff) == 1:
            print 'Case #'+str(prob+1)+': ' + list(diff)[0]
        elif len(diff) > 1:
            print 'Case #'+str(prob+1)+': Bad magician!'
        else:
            print 'Case #'+str(prob+1)+': Volunteer cheated!'
        

if __name__ == "__main__":
    main()
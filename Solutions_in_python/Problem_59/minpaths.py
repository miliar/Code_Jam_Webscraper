import sys

from twisted.python.filepath import FilePath

def readCase(fObj):
    extant, create = map(int, fObj.readline().split())
    extant = set(FilePath(fObj.readline().strip()) for i in range(extant))
    extant.add(FilePath('/'))
    create = set(FilePath(fObj.readline().strip()) for i in range(create))
    return extant, create


def solveCase(extant, create):
    count = 0
    for leaf in create:
        node = leaf
        while node not in extant:
            extant.add(node)
            count += 1
            node = node.parent()
    return count


def main():
    case = 1
    numCases = int(sys.stdin.readline())
    for case in range(numCases):
        extant, create = readCase(sys.stdin)
        result = solveCase(extant, create)
        print 'Case #%d: %d' % (case + 1, result)

if __name__ == '__main__':
    main()

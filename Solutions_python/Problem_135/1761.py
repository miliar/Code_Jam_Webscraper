import sys

input = []

def parse_file(filePath):
    with open(filePath) as f:
        T = int(f.readline())
        for i in range(1, T + 1):
            firstAnswer = int(f.readline())
            firstArrangement = []
            for j in range(4):
                firstArrangement.append([int(x) for x in f.readline().split()])
            secondAnswer = int(f.readline())
            secondArrangement = []
            for j in range(4):
                secondArrangement.append([int(x) for x in f.readline().split()])
            input.append((firstAnswer, firstArrangement, secondAnswer, secondArrangement))
            
def main():
    parse_file(sys.argv[1])
    i = 1
    for row1, grid1, row2, grid2 in input:
        res = set(grid1[row1 - 1]) & set(grid2[row2 - 1])
        if len(res) == 0:
            print('Case #%d: Volunteer cheated!' % i)
        elif len(res) == 1:
            print('Case #%d: %d' % (i, next(iter(res))))
        else:
            print('Case #%d: Bad magician!' % i)
        i = i + 1

if __name__ == '__main__':
    main()    

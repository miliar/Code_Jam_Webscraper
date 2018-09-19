from math import log10, ceil

class Case:
    @classmethod
    def parse(cls, line):
        data = list(map(int, line.split()))
        assert len(data) == 3
        return Case(*data)

    def __init__(self, rows, cols, width):
        self.rows = rows
        self.cols = cols
        self.width = width

    def solve(self):
        rows = self.rows
        cols = self.cols
        width = self.width

        moves = 0
        if rows>1:
            moves += (rows-1)*(cols//width)
        moves += self.calcLastRow()
        return moves

    def calcLastRow(self):
        cols = self.cols
        width = self.width
        extraMiss = (cols % width != 0)
        points = cols//width + width - 1
        if extraMiss:
            points += 1
        return points

def main(finname, foutname=None):
    fin = open(finname, 'r')
    fout = None if foutname==None else open(foutname, 'w')
    count = int(next(fin).strip())
    for i in range(count):
        case = Case.parse(next(fin).strip())
        print("Case #{}: {}".format(i+1, case.solve()), file=fout)

if __name__ == '__main__':
    #assert(rev(12345) == 54321)
    main("A-large.in", "A-large.out")
    #main("input.txt")

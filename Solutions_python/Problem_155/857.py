class Case:
    @classmethod
    def parse(cls, line):
        Smax, values = line.split(' ')
        return Case(int(Smax), map(int, values))

    def __init__(self, Smax, values):
        self.Smax = Smax
        self.values = values

    def solve(self):
        values = self.values
        totalStanding = 0
        add = 0
        for i, Si in enumerate(self.values):
            if Si>0 and totalStanding < i:
                add += (i-totalStanding)
                totalStanding = i
            totalStanding += Si
        return add

def main(finname, foutname=None):
    fin = open(finname, 'r')
    fout = None if foutname==None else open(foutname, 'w')
    count = int(next(fin).strip())
    for i in range(count):
        case = Case.parse(next(fin).strip())
        print("Case #{}: {}".format(i+1, case.solve()), file=fout)

if __name__ == '__main__':
    main("A-large.in", "A-large.out")
from collections import defaultdict


class State:
    def __init__(self, plates, splits=0):
        self.plates = plates
        self.splits = splits
        plates.sort()

    def getMinutes(self):
        return max(self.plates) + self.splits

    def __hash__(self):
        return hash(" ".join(map(str, self.plates)) + " " + str(self.splits))

    def iterSplits(self):
        maxPlate = max(self.plates)
        if maxPlate == 1:
            raise StopIteration
        tail = self.plates[:]
        tail.remove(maxPlate)
        for i in range(1, maxPlate//2+1):
            yield State(tail + [i, maxPlate-i], self.splits+1)


class Case:
    @classmethod
    def parse(cls, stream):
        line1 = next(stream)
        plates = map(int, next(stream).strip().split(' '))
        return cls(list(plates))

    def __init__(self, plates):
        self.plates = plates

    def solve(self):
        states = [State(self.plates)]
        minMinutes = states[0].getMinutes()

        hashes = set()
        hashes.add(hash(states[0]))

        for s in states:
            if s.splits > minMinutes:
                continue
            for s2 in s.iterSplits():
                if hash(s2) not in hashes:
                    minMinutes = min(minMinutes, s2.getMinutes())
                    states.append(s2)
        return minMinutes


def main(finname, foutname=None):
    fin = open(finname, 'r')
    fout = None if foutname==None else open(foutname, 'w')
    count = int(next(fin).strip())
    for i in range(count):
        case = Case.parse(fin)
        print("Case #{}: {}".format(i+1, case.solve()), file=fout)

if __name__ == '__main__':
    main("B-small-attempt1.in", "B-small-attempt1.out")

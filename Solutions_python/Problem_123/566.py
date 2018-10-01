import sys


class Osmos(object):
    def __init__(self, armin, motes):
        self.armin = armin
        self.motes = motes
    def solve(self):
        #print self
        self.absorb()
        if len(self.motes) > 0:
            return self.step()
        #raw_input()
        return 0
    def absorb(self):
        to_remove = []
        for index, mote in enumerate(self.motes):
            if mote < self.armin:
                self.armin += mote
                to_remove.append(index)
            else:
                break
        self.motes = self.motes[len(to_remove):]
    def step(self):
        remove = Osmos(self.armin, self.motes[1:]).solve()
        if self.armin * 2 - 1 != self.armin:
            add = Osmos(self.armin * 2 - 1, self.motes).solve()
        else:
            add = remove
        return 1 + min(add, remove)

    def __str__(self):
        return "%d: %s" % (self.armin, ','.join(map(str, self.motes)))

def get_osmos(infile):
    armin, n = map(int, infile.readline().split())
    motes = map(int, infile.readline().split())
    motes.sort()
    return Osmos(armin, motes)

filename = sys.argv[1]
with open(filename)as infile:
    with open('.'.join([filename.split('.')[0], 'out']), 'w') as outfile:
        cases = int(infile.readline())
        for case in range(cases):
            osmos = get_osmos(infile)
            steps = osmos.solve()
            solution = "Case #%d: %d\n" % (case + 1, steps)
            outfile.write(solution)

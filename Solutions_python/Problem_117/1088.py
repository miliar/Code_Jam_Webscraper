import sys
import numpy

class Lawn(object):
    def __init__(self, data):
        self.grass = numpy.array([map(int, d.split()) for d in data])

    def test(self):
        if self.grass.max() > 100:
            return False
        return ((self.grass >= self.grass.max(0)) |
                (self.grass.T >= self.grass.max(1)).T).all()

data = open(sys.argv[1]).read().splitlines()
i = 1
lawns = []
while i < len(data):
    n = int(data[i].split()[0])
    i += 1
    lawns.append(Lawn(data[i:i+n]))
    i += n

for n,l in enumerate(lawns):
    print 'Case #%i: %s' % (n+1, 'YES' if l.test() else 'NO')
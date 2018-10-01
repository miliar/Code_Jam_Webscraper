__author__ = 'Mohan.Rajendran'
class Quaternion:
    def __init__(self, sign, item):
        self.sign = sign
        self.item = item

    @classmethod
    def create(cls, item):
        return cls(1, item)

    def __str__(self):
        if self.sign == 1:
            return self.item
        else:
            return '-' + self.item

    def __mul__(self,other):
        sign = self.sign * other.sign

        if self.item == '1':
            carry = 1
            item = other.item
        elif self.item == other.item:
            carry = -1
            item = '1'
        elif other.item == '1':
            carry = 1
            item = self.item
        elif self.item == 'i':
            if other.item == 'j':
                carry = 1
                item = 'k'
            else:
                carry = -1
                item = 'j'
        elif self.item == 'j':
            if other.item == 'i':
                carry = -1
                item = 'k'
            else:
                carry = 1
                item = 'i'
        else:
            if other.item == 'i':
                carry = 1
                item = 'j'
            else:
                carry = -1
                item = 'i'

        return Quaternion(sign*carry, item)

def solve(inp):
    lx = inp.readline().split()
    L = int(lx[0])
    X = int(lx[1])
    S = inp.readline().rstrip()

    if L*X < 3:
        return 'NO'

    Sq = map(lambda x: Quaternion.create(x), S)
    Smul = reduce(Quaternion.__mul__, Sq, Quaternion.create('1'))

    Stot = reduce(Quaternion.__mul__, [Smul for i in xrange(X)], Quaternion.create('1'))

    if Stot.item != '1' or Stot.sign != -1:
        return 'NO'

    phase = 1
    prod = Quaternion.create('1')
    for x in xrange(X):
        for s in S:
            prod *= Quaternion.create(s)
            if prod.sign == 1 and prod.item == 'i' and phase == 1:
                phase = 2
                prod = Quaternion.create('1')
            if prod.sign == 1 and prod.item == 'j' and phase == 2:
                return 'YES'

    return 'NO'

if __name__ == "__main__":
    fileName = "small"
    inp = open(fileName + '.in', 'r')
    outp = open(fileName + '.out', 'w')

    cases = int(inp.readline())

    for case in xrange(1, cases+1):
        outp.write("Case #%i: %s\n" % (case, solve(inp)))

    inp.close()
    outp.close()
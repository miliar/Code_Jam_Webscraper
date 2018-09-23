import sys
sys.stdin = open('input/B-small-attempt2.in', 'r')
sys.stdout = open('out/B-small-attempt2.out', 'w')

class Aux:
    def __init__(self, R, O, Y, G, B, V):
        self.symbols = [
            {'symbol': 'R', 'number': R},
            {'symbol': 'O', 'number': O},
            {'symbol': 'Y', 'number': Y},
            {'symbol': 'G', 'number': G},
            {'symbol': 'B', 'number': B},
            {'symbol': 'V', 'number': V},
        ]
        self.symbols = sorted(self.symbols, key=lambda x: x['number'], reverse=True)
        self.last = ''

    def next(self):
        max = 0
        for val in self.symbols:
            if val['symbol'] != self.last and val['number'] > max:
                max = val['number']
                max_item = val

        max_item['number'] -= 1
        self.last = max_item['symbol']
        return max_item['symbol']


t = int(raw_input())
for i in range(t):
    N, R, O, Y, G, B, V = [int(s) for s in raw_input().split(" ")]
    if R > float(N) / 2 or Y > float(N) / 2 or B > float(N) / 2:
        print "Case #{}: IMPOSSIBLE".format(i+1)
    else:
        aux = Aux(R, O, Y, G, B, V)
        sorting = ''.join([aux.next() for _ in range(N)])
        print "Case #{}: {}".format(i+1, ''.join(sorting))

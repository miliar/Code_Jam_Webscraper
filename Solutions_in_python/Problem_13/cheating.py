from sys import maxint as infinity
from pprint import pprint

N = int(raw_input())

class Node:
    def __init__ (self, gate, changeable):
        self.gate = gate
        self.changeable = changeable

class Leaf:
    def __init__ (self, value):
        self.value = value

for case in range(1, N+1):
    m, v = map(int, raw_input().split())

    tree = []
    best = [[infinity, infinity] for _ in range(m)]

#    pprint(best)

    for i in range((m-1)//2):
        g, c = map(int, raw_input().split())
        tree.append(Node(g, c))

    for i in range((m+1)//2):
        value = int(raw_input())
        tree.append(Leaf(value))

    for i in range(m-1, -1, -1):
        n = tree[i]

        if isinstance(n, Leaf):
            best[i][n.value] = 0
        else:
            n.value = int(bool([tree[2*i+1].value or tree[2*i+2].value,
                        tree[2*i+1].value and tree[2*i+2].value][n.gate]))
            best[i][n.value] = 0

            if n.value:
                # trying to get False
                if n.gate == 0: # or
                    best[i][0] = best[2*i+1][0] + best[2*i+2][0]
                    if n.changeable:
                        best[i][0] = min(best[i][0],
                                         1 + best[2*i+1][0],
                                         1 + best[2*i+2][0]) # change to and
                else:
                    best[i][0] = min(best[2*i+1][0],
                                         best[2*i+2][0])
            else:
                if n.gate == 0: # or
                    best[i][1] = min(best[2*i+1][1], best[2*i+2][1])
                else:
                    best[i][1] = best[2*i+1][1] + best[2*i+2][1]
                    if n.changeable:
                        best[i][1] = min(best[i][1],
                                         1 + best[2*i+1][1],
                                         1 + best[2*i+2][1]) # change to or

        #pprint(best)
    
    ans = best[0][v]
    print 'Case #%i: %s' % (case, ans if ans < infinity else 'IMPOSSIBLE')

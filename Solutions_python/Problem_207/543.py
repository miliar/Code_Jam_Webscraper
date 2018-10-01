#NTheo
from __future__ import division

T = int(raw_input())
for t in range(T):
    G = {}
    N, G['R'], G['O'], G['Y'], G['G'], G['B'], G['V'] = [int(x) for x in raw_input().split()]
    w_list = []
    def park(color):
        w_list.append(color)
        G[color] -= 1
        return color
    for color in 'RYB':
        if G[color] > 0:
            current = park(color)
            break
    else:
        print('Case #{}: IMPOSSIBLE'.format(t+1))
        break
    for n in range(N-1):
        if current == 'R':
            if G['G']>0:
                current = park('G')
            elif G['Y'] == max(G['Y'], G['B']):
                current = park('Y')
            else:
                current = park('B')
        elif current == 'Y':
            if G['V']>0:
                current = park('V')
            elif G['R'] == max(G['R'], G['B']):
                current = park('R')
            else:
                current = park('B')
        elif current == 'B':
            if G['O']>0:
                current = park('O')
            elif G['R'] == max(G['R'], G['Y']):
                current = park('R')
            else:
                current = park('Y')
        elif current == 'G':
            current = park('R')            
        elif current == 'V':
            current = park('Y')
        elif current == 'O':
            current = park('B')
    for v in G.values():
        if v<0:
            print('Case #{}: IMPOSSIBLE'.format(t+1))
            break
    else:
        w = ''.join(w_list)
        if w[0] == w[-1] or w[0] == 'R' and w[-1] in 'OV' or w[0] == 'Y' and w[-1] in 'GO' or w[0] == 'B' and w[-1] == 'VG':
            print('Case #{}: IMPOSSIBLE'.format(t+1))
        else:
            print('Case #{}: {}'.format(t+1, w)) 

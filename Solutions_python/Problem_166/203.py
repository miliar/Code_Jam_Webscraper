from itertools import product

T = int(input())
for t in range(1,T+1):
    K, L, S = [ int(x) for x in input().split() ] 
    keyboard = input()
    target = input()

    poc = 0
    total = 0
    m = 0
    for typed in product(keyboard, repeat=S):
        keys = ''.join(typed)
        count = sum([ keys[i:i+L] == target for i in range(S-L+1) ])
        poc += count
        m = max(m, count)
        total += 1
    print('Case #%d: %.7f' % (t, m - float(poc) / float(total)))

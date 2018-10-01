from collections import defaultdict

def solve(arr):
    c = int(arr[0])
    combo = {}
    for s in arr[1:c + 1]:
        x, y, z = s
        combo[x+y] = z
        combo[y+x] = z
    arr = arr[c + 1:]
    d = int(arr[0])
    opposed = defaultdict(list)
    for s in arr[1:d + 1]:
        a, b = s
        opposed[a].append(b)
        opposed[b].append(a)
    lst = []
    for char in arr[-1].strip():
        lst.append(char)
        if len(lst) > 1:
            try:
                rep = combo[lst[-2]+lst[-1]]
                lst.pop()
                lst.pop()
                lst.append(rep)
                continue
            except KeyError:
                pass
        for opp in opposed[char]:
            if opp in lst:
                lst = []
                continue
    return '[' + ', '.join(lst) + ']'


with open ('B-large.in') as f:
    t = int(f.readline())
    for i in range(t):
        arr = f.readline().split(' ')
        print 'Case #{0}: {1}'.format(i+1 ,solve(arr))

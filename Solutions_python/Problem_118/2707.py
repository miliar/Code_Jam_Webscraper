fi = open('C.in')
fo = open('C.out', 'w')
def line():
    return fi.next().strip()
n = int(line())
fair_square = []

def is_pal(s):
    if len(s) in (0, 1):
        return True
    return s[0] == s[-1] and is_pal(s[1:-1])
for i in range(1, 10**7 + 1):
    if is_pal(str(i)) and is_pal(str(i * i)):
        fair_square.append(i * i)
for i in range(1, n + 1):
    a, b = map(int, line().split())
    idx = 0
    cnt = 0
    for j in range(a, b + 1):
        while j > fair_square[idx]:
            idx += 1
        if j == fair_square[idx]:
            idx += 1
            cnt += 1
            
    fo.write('Case #%d: %d\n' %(i, cnt))

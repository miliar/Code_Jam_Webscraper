rd = input

def ints():
    return list(map(int, rd().split()))

def solve(d, kss):
    t = max((d - k)/s for k,s in kss)
    return d/t

for t in range(int(rd())):
    d, n = ints()
    print('Case #{}: {}'.format(t+1, solve(d, [ints() for _ in range(n)]))) 

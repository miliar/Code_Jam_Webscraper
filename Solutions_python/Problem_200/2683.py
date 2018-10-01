def solve(n):
    if n[0:2] == '10':
        return '9'*(len(n)-1)
    i = 0
    while i < len(n)-1:
        if n[0:2] == '10':
            return '9'*(len(n)-1)
        if n[i] > n[i+1]:
            n = n[:i+1] + ['9' for c in range(len(n[i+1:]))]
            n[i] = str(int(n[i])-1) 
            i = 0
        else:
            i = i + 1
    while n[0] == '0':
        n.pop(0)
    return ''.join(n)

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\B-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        n = [c for c in r.readline().strip()]
        w.write('Case #{0}: {1}\n'.format(case, solve(n)))
        

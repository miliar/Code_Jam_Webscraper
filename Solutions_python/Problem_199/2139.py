def solve(s, m):
    cnt = 0
    for i in range(len(s)-m+1):
        if s[i] == '-':
            cnt += 1
            for j in range(i, i+m):
                s[j] = '+' if s[j] == '-' else '-'

    for c in s:
        if c == '-':
            return "IMPOSSIBLE"

    return str(cnt)

fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

t = int(fin.readline())

for i in range(t):
    ins = fin.readline().split()
    s = list(ins[0])
    m = int(ins[1])
    fout.write("Case #" + str(i+1) + ": " + solve(s, m) + "\n")

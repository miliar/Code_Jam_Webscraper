with open('B-large.in', 'r') as f:
    lines = f.readlines()
T = int(lines[0].strip())
lines = lines[1:T+1]

g = open('B_large_output.txt', 'w')

for t, line in enumerate(lines):
    x = [int(x) for x in line.strip()]
    L = len(x)
    pos = L
    for i in range(L-1, 0, -1):
        if x[i-1] > x[i]:
            x[i-1] -= 1
            pos = i
    for i in range(pos, L):
        x[i] = 9
    x = [str(y) for y in x if y != 0]
    # print('Case #%d: ' % (t+1) + ''.join(x))
    g.write(('Case #%d: ' % (t+1) + ''.join(x)) + '\n')

g.close()

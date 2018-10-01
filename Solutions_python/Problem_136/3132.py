from sys import stdin, stdout

res = []
for i, line in enumerate(stdin.readlines()[1:], 1):
    r, t = 2.0, 0
    c, f, x = map(float, line.split())

    if x <= c:
        t = x / r
    else:
        while True:
            if x / r < c / r + x / (r+f):
                t += x / r
                break
            else:
                t += c / r
                r += f
    res.append('Case #{}: {:.7f}'.format(i, t))
stdout.writelines('\n'.join(res))

>>> file(r'c:\var\tmp\out.txt', 'w').write(''.join(['Case #%d: %d\n' % (i+1, ans
wer) for (i, answer) in enumerate(map(lambda xs: (lambda s, p, t: (lambda (x1, x
2): x1 + min(x2 - x1, s))(map(lambda l: len(filter(lambda x: x >= l, t)),(p + 2*
max(p-1, 0), p + 2*max(p-2, 0)))))(xs[1], xs[2], xs[3:]),[(map(int, line.split()
)) for line in file(r'c:\var\tmp\in.txt').readlines() if line][1:]))]))
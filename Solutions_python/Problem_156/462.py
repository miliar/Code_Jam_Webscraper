from sys import stdin, stdout

T = int(stdin.readline().strip())

for case in range(1,T+1):
    stdin.readline() # ignore the first line
    ps = map(int, stdin.readline().strip().split())
    best = max(ps)
    for i in range(1, best+1):
        total = sum([ (p-1) // i for p in ps ]) + i
        if total < best:
            best = total
    stdout.write("Case #{:d}: {:d}\n".format(case, best))

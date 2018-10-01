import sys

T = int(sys.stdin.readline())

def best(n, p):
    if n < 3:
        if n == 0:
            if p == 0: return (1, 0)
            else: return (0, 0)
        elif n == 1:
            if p <= 1: return (1, 0)
            else: return (0, 0)
        else:
            if p <= 1: return (1, 0)
            elif p == 2: return (0, 1)
            else: return (0, 0)
    else:
        test = n / 3
        if n % 3 == 0:
            if p <= test: return (1, 0)
            elif p == test + 1: return (0, 1)
            else: return (0, 0)
        elif n % 3 == 1:
            if p <= test + 1: return (1, 0)
            else: return (0, 0)
        else:
            if p <= test + 1: return (1, 0)
            elif p == test + 2: return (0, 1)
            else: return (0, 0)

for case in xrange(1, T+1):
    line = sys.stdin.readline()
    line_arr = [int(x) for x in line.split()]
    N = line_arr[0]
    S = line_arr[1]
    p = line_arr[2]
    scores = line_arr[3:]
    results = [best(x, p) for x in scores]
    normals = sum([x[0] for x in results])
    outstandings = sum([x[1] for x in results])
    outstandings_trimmed = min(outstandings, S)
    sys.stdout.write("Case #"+str(case)+": ")
    sys.stdout.write(str(normals + outstandings_trimmed))
    if case != T:
        sys.stdout.write("\n")
    

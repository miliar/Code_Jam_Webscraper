f = open('test')
g = open('out', 'w')
test_cases = int(f.readline())
for case in range(0, test_cases):
    inp = f.readline().split()
    n = int(inp[0])
    s = int(inp[1])
    p = int(inp[2])
    max = 0
    scores = [int(i) for i in inp[3:]]
    for score in scores:
        if p == 0:
            max += 1
            continue
        if score >= 3*p-2 :
            max += 1
        elif score >= 3*p - 4 and s > 0 and 3*p-4 >= 0:
            max += 1
            s -= 1
        else :
            pass
    g.write("Case #{}: {}\n".format(case+1, max))
f.close()
g.close()

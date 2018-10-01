in_file = 'C-small-attempt1.in'
out_file = 'C-small.out'
inp = open(in_file, 'r')
out = open(out_file, 'w')

t = int(inp.readline())
for case in range(1, t+1):
    n, q = list(map(int, inp.readline().split()))
    e = []
    s = []
    for i in range(n):
        new_e, new_s = list(map(int, inp.readline().split()))
        e.append(new_e)
        s.append(new_s)
    d = []
    for i in range(n-1):
        new_d = list(map(int, inp.readline().split()))
        d.append(new_d[i+1])

    inp.readline()
    inp.readline()

    shortest_time = [0]
    shortest_time.append(d[0]/s[0])

    for i in range(2, n):
        t = float('inf')
        for j in range(i):
            if e[j] >= sum(d[j:i]):
                if shortest_time[j] + sum(d[j:i])/s[j] < t:
                    t = shortest_time[j] + sum(d[j:i])/s[j]
        shortest_time.append(t)

    out.write('Case #{}: {}\n'.format(case, shortest_time[n-1]))

inp.close()
out.close()

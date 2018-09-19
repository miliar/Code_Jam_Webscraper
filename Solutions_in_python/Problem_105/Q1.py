def BFS(d, start):
    dia_visited = []
    to_visit = [start]
    while to_visit:
        now = to_visit.pop(0)
        dia_visited.append(now)
        for dia in d[now]:
            if (dia in dia_visited) or (dia in to_visit):
                return True
            else:
                to_visit.append(dia)
    return False

if __name__ == '__main__':
    #f = open('sample.in')
    #output = open('sample.out', 'w')
    f = open('A-large.in')
    output = open('A-large.out', 'w')
    test_case = int(f.readline())
    for i in range(test_case):
        N = int(f.readline())
        d = {}
        start = []
        for j in range(1, N+1):
            d[j] = []
        for j in range(1, N+1):
            line = f.readline()
            line = line.split()
            M = int(line[0])
            if M == 0:
                start.append(j)
            line = [int(line[k]) for k in range(1, M+1)]
            for dia in line:
                d[dia].append(j)
        s = 'Case #%s: ' %(i+1)
        for sta in start:
            result = BFS(d, sta)
            if result:
                output.write(s + 'Yes\n')
                break
        if not result:
            output.write(s + 'No\n')
    f.close()
    output.close()
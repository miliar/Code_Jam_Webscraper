def get_previous_neat_int(N):
    if N <= 9:
        return N
    n = str(N)
    first = []
    prev = []
    cur = 0
    for i in xrange(len(n) - 1):
        prev.append(int(n[i]))
        cur = int(n[i+1])
        if cur < prev[-1]:
            prev = map(lambda x: x-1, prev)
            if prev[-1] == 0:
                first = [9] * (len(n) - 1)
            else:
                rest = [9] * (len(n) - len(first) - 1)
                first.append(prev[0])
                first.extend(rest)
            neat = 0
            for i in xrange(len(first)):
                neat += first[::-1][i] * (10 ** i)
            # print N, ' -> ', neat
            return neat
        elif cur !=  prev[-1]:
            first.extend(prev)
            prev = []
    return N

if __name__ == '__main__':
    with open('B-large.in', 'r') as infile:
        # test_csv = csv.reader(test_fh, delimiter=',', quotechar='"')
        T = int(next(infile))
        with open('B-large.out', 'w') as outfile:
            # soln_csv = csv.writer(soln_fh, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            case = 0
            for line in infile:
                case += 1
                sol = get_previous_neat_int(int(line))
                print int(line), '->', sol
                outfile.write('Case #{}: {}\n'.format(case, sol))

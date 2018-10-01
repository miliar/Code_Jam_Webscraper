

def solve(d):
    n = len(d)
    m = len(d[0])
    lines_max = [max(line) for line in d]
    column_max = [max([d[i][j] for i in range(n)]) for j in range(m)]

    for i in range(n):
        for j in range(m):
            p = d[i][j]
            if p < lines_max[i] and p < column_max[j]:
                return 'NO'
    return 'YES'


if __name__ == '__main__':
    n = input()
    for i in range(n):
        m = int(raw_input().split(' ')[0])
        d = [map(int, raw_input().split(' ')) for j in range(m)]
        print('Case #{}: {}'.format(i + 1, solve(d)))

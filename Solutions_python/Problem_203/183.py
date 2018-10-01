

D4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def solve(r, c, cake):
    initials = []
    for i in range(r):
        for j in range(c):
            if cake[i][j] != '?':
                initials.append((i, j , cake[i][j]))
    for i in range(len(initials)):
        y,x,w = initials[i]
        nx = x-1
        while 0<=nx and cake[y][nx] == '?':
            cake[y][nx] = w
            nx -= 1
        nx = x+1
        while nx<c and cake[y][nx] == '?':
            cake[y][nx] = w
            nx += 1

    if cake[0][0] == '?':
        for i in range(1, r):
            if cake[i][0] != '?':
                for j in range(i):
                    for k in range(c):
                        cake[j][k] = cake[i][k]
                break
    for i in range(r-1):
        for j in range(c):
            if cake[i+1][j] == '?':
                cake[i+1][j] = cake[i][j]


    ret = '\n'.join([''.join(cake[i]) for i in range(r)])
    return ret

def print_answer(t, ans):
    tmpl = 'Case #{0}:\n{1}'
    print(tmpl.format(t+1, ans))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        R,C = map(int, input().split())
        cake = [[x for x in input()] for i in range(R)]
        ans = solve(R,C,cake)
        print_answer(_, ans)
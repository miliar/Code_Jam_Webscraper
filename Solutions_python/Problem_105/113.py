from sys import stdin


def solve():
    T = int(stdin.readline())
    for casenum in range(T):
        result = solve_case()
        print 'Case #%d: %s' % (casenum + 1, result)

def solve_case():
    n = int(stdin.readline())
    a = [[]]
    for i in range(n):
        a.append([int(x) for x in stdin.readline().split()][1:])
    for s in range(n+1):
        clr = [0] * (n+1)
        clr[s] = 1
        q = [s]
        while len(q) > 0:
            u = q[0]
            for v in a[u]:
                if clr[v] == 0:
                    clr[v] = 1
                    q.append(v)
                else:
                    return 'Yes'
            q = q[1:]

    return 'No'


if __name__ == '__main__':
    solve()

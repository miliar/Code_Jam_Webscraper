import sys

def solve():
    T = int(sys.stdin.readline())
    
    for tc in range(T):
        N = int(sys.stdin.readline())
        ans = get_last_tidy(N)

        print('Case #{}: {}'.format(tc + 1, ans))

def get_last_tidy(m):
    ml = [int(i) for i in str(m)]
    p = 0

    for j in range(len(ml) - 1):
        if ml[j] < ml[j + 1]:
            p = j + 1
        elif ml[j] > ml[j + 1]:
            for k in range(p + 1, len(ml)):
                ml[k] = 9

            ml[p] -= 1

            break

    # print(ml, file=sys.stderr)

    if ml[0] == 0:
        res = '9' * (len(ml) - 1)
        res = int(res)
    else:
        res = ''.join([str(i) for i in ml])
        res = int(res)

    return res

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

if __name__ == '__main__':
    solve()
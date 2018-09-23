import sys

def solve():
    T = int(sys.stdin.readline())

    for tc in range(T):
        N, R, O, Y, G, B, V = map(int, sys.stdin.readline().split())

        M = max(R, Y, B)

        if M > N // 2:
            ans = 'IMPOSSIBLE'
        else:
            ans = '#'

            if M == R:
                con = 'R'
            elif M == Y:
                con = 'Y'
            else:
                con = 'B'

            for i in range(N):
                if ans[-1] != con and M > 0:
                    ans += con
                    M -= 1
                else:
                    if con == 'R':
                        if Y < B:
                            ans += 'B'
                            B -= 1
                        else:
                            ans += 'Y'
                            Y -= 1
                    elif con == 'Y':
                        if R < B:
                            ans += 'B'
                            B -= 1
                        else:
                            ans += 'R'
                            R -= 1
                    elif con == 'B':
                        if R < Y:
                            ans += 'Y'
                            Y -= 1
                        else:
                            ans += 'R'
                            R -= 1
                    else:
                        raise

            ans = ans.lstrip('#')

        print('Case #{}: {}'.format(tc + 1, ans))


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

if __name__ == '__main__':
    solve()
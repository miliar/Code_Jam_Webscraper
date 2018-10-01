def is_tidy(n: int) -> bool:
    return ''.join(sorted(str(n))) == str(n)


def generate_tidy_number(n: int) -> str:
    lst = [int(x) for x in str(n)]
    idx = len(lst) - 1
    while idx > 0:
        if lst[idx] < lst[idx - 1]:
            lst[idx - 1] -= 1
            for idy in range(idx, len(lst)):
                lst[idy] = 9
        idx -= 1
    if lst[0] == 0:
        return ''.join(map(str, lst[1:]))
    else:
        return ''.join(map(str, lst))


def solve() -> None:
    T = int(input())
    for idx in range(T):
        n = int(input())
        print('Case #{}: {}'.format(idx + 1, generate_tidy_number(n)))


if __name__ == '__main__':
    solve()

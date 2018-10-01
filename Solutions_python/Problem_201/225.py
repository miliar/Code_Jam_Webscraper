def solve():
    n, k = map(int, input().split())
    vals = {n: 1}
    while True:
        space = max(vals.keys())
        count = vals.pop(space)
        space -= 1
        small = space // 2
        large = space - small
        if count >= k:
            return '{} {}'.format(large, small)
        k -= count
        vals[small] = count + vals.get(small, 0)
        vals[large] = count + vals.get(large, 0)


def main():
    t = int(input())
    for i in range(t):
        print('Case #{}: {}'.format(i + 1, solve()))


if __name__ == '__main__':
    main()

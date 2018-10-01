def solve():
    n, k = map(int, input().split())
    u = float(input())
    p = list(map(float, input().split()))
    if (n == k):
        p.sort()
        for i in range(1, n):
            if (p[i] - p[i - 1]) * i <= u:
                u -= (p[i] - p[i - 1]) * i
                for j in range(i):
                    p[j] = p[i]
            else:
                for j in range(i):
                    p[j] += u / i
                u = 0
                break
        if u > 0:
            for i in range(n):
                p[i] += u / n
        ans = 1
        for i in p:
            ans *= i
        return ans
    return None


def main():
    tests = int(input())
    for test in range(1, tests + 1):
        print('Case #{}: {}'.format(test, solve()))

if __name__ == '__main__':
    main()

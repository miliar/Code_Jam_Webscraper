import math

def solve():
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        r, h = map(int, input().split())
        a.append((r, h))
    a.sort(key = lambda x: x[0] * x[1], reverse = True)
    answer = 0
    for i in range(n):
        current = a[i][0] * a[i][1]
        left = k - 1
        for j in range(n):
            if j != i and a[j][0] <= a[i][0]:
                if not left:
                    break
                current += a[j][0] * a[j][1]
                left -= 1
        if left:
            continue
        current = current * 2 * math.pi + math.pi * (a[i][0] ** 2)
        answer = max(current, answer)
    return answer


def main():
    tests = int(input())
    for test in range(1, tests + 1):
        print('Case #{}: {}'.format(test, solve()))

if __name__ == '__main__':
    main()

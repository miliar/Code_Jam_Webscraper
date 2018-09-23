import math

def smple_syrup(pancakes, K):
    areas = sorted([(r * r, r * h * 2) for r, h in pancakes], reverse=True)

    result = 0
    for i in range(len(pancakes) - K + 1):
        temp = sum(areas[i]) + sum(sorted((y for x, y in areas[i + 1:]), reverse=True)[:K-1])
        result = max(temp, result)

    return math.pi * result

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        pancakes = [tuple(map(int, input().split())) for _ in range(N)]

        result = smple_syrup(pancakes, K)

        print("Case #{}: {}".format(i + 1, result))


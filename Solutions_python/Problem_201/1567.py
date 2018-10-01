
import heapq


def pop(heap):
    return -heapq.heappop(heap)


def push(heap, number):
    heapq.heappush(heap, -number)

T = int(input())
lines = []
for _ in range(T):
    lines.append(input().split(" "))

for case, line in enumerate(lines):
    N = int(line[0])
    K = int(line[1])
    numbers = []
    push(numbers, N)
    for _ in range(K - 1):
        n = pop(numbers)
        if n % 2 == 0:
            push(numbers, n // 2)
            push(numbers, n // 2 - 1)
        else:
            for _ in range(2):
                push(numbers, n // 2)
    n = pop(numbers)
    if n % 2 == 0:
        minimum, maximum = n // 2 - 1, n // 2
    else:
        minimum, maximum = n // 2, n // 2
    print("Case #{}: {} {}".format(case + 1, maximum, minimum))

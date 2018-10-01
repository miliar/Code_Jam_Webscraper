MAXN = 10 ** 18

all_numbers = list(range(1, 10))
i = 0
while i < len(all_numbers):
    if all_numbers[i] >= MAXN:
        break
    for j in range(all_numbers[i] % 10, 10):
        all_numbers.append(all_numbers[i] * 10 + j)
    i += 1

for i in range(1, int(input()) + 1):
    n = int(input())
    result = 0
    for c in all_numbers:
        if n >= c:
            result = c 
        else:
            break
    print('Case #{}: {}'.format(i, result))

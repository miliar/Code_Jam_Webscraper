import sys
import bisect

def cnk(n, k):
    if k == 0:
        return int(n > 0)
    res = 1
    for i in range(n - k + 1, n + 1):
        res *= i
    for i in range(1, k + 1):
        res //= k
    return res

def cnk_ext(n, k):
    if k == 0:
        return 1
    return cnk(n + k - 1, k)

def calc_len(n):
    res = 0
    for i in range(9):
        res += cnk_ext(n, i)

    return res

pw_11 = [1]
for i in range(20):
    pw_11.append(pw_11[-1] * 10 + 1)

def calc_number(stack):
    res = 0
    for x in stack:
        res += pw_11[x]
    return res

def gen_numbers_inner(num_to_place, cur_col, stack):
    if num_to_place == 0 or cur_col == -1:
        return [calc_number(stack)]

    res = []
    res.extend(gen_numbers_inner(num_to_place, cur_col - 1, stack))

    for place_here in range(1, num_to_place + 1):
        stack.append(cur_col)
        res.extend(gen_numbers_inner(num_to_place - place_here, cur_col - 1, stack))

    for i in range(1, num_to_place + 1):
        stack.pop()

    return res

def gen_numbers(sz):
    base = [sz - 1]
    answer = []
    answer.extend(gen_numbers_inner(8, sz - 1, base))

    return answer

numbers = []
for n in range(1, 19):
    cur = calc_len(n)
    cur_numbers = gen_numbers(n)
    numbers.extend(cur_numbers)
    print(n, len(numbers))
    sys.stdout.flush()

numbers.append(10 ** 18 + 12)
t = int(input())
for i in range(1, t + 1):
    x = int(input())
    answer_idx = bisect.bisect_right(numbers, x)
    answer_idx -= 1
    print('Case #{}: {}'.format(i, numbers[answer_idx]))

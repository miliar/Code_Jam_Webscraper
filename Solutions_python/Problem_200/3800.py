import logging

logging.basicConfig(level=logging.WARN)


def last_tidy(n):
    logging.debug(n)
    if n < 10:
        return n
    digits = [int(x) for x in str(n)]
    # left to right
    left = 0
    right = left + 1
    while right < len(digits):
        if digits[left] > digits[right]:
            digits[left] = digits[left] - 1
            for i in range(right, len(digits)):
                digits[i] = 9
            break
        left = right
        right += 1
    logging.debug('first pass: {}'.format(digits))
    # right to left
    right = len(digits) - 1
    left = right - 1
    while left > -1:
        if digits[left] > digits[right]:
            digits[left] = digits[left] - 1
            digits[right] = 9
        right = left
        left = right - 1
    ans = ''.join([str(x) for x in digits])
    logging.info(ans)
    return int(ans)


T = int(input())
for case in range(1, T+1):
    n = int(input())
    print('Case #{}: {}'.format(case, last_tidy(n)))

import sys

def tidy(n):
    digits = [int(d) for d in str(n)]
    for i in reversed(range(len(digits) - 1)):
        if digits[i + 1] < digits[i]:
            digits[i] -= 1
            for j in range(i + 1, len(digits)):
                digits[j] = 9
    return int(''.join(str(d) for d in digits))

tc_len = int(sys.stdin.readline())
for tc in range(tc_len):
    n = int(sys.stdin.readline())
    print('Case #' + str(tc + 1) + ': ' + str(tidy(n)))

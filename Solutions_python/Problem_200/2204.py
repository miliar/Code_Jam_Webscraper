def ascend(digits, i):
    if i == len(digits):
        return (9, i)
    if i > 0 and digits[i] < digits[i-1]:
        olddigit = digits[i]
        digits[i] = 9
        return (olddigit, i)
    else:
        num, j = ascend(digits, i+1)
        if j == i+1 and num < digits[i]:
            digits[i] -= 1
            return (digits[i], i)
        else:
            return (9, j)

T = int(input())
for _ in range(T):
    N = input()
    digits = [int(c) for c in N]
    _x, j = ascend(digits, 0)
    newdigits = [(digits[i] if i <= j else 9) for i in range(len(digits))]
    print("Case #" + str(_+1) + ": " + str(int("".join(map(str, newdigits)))))

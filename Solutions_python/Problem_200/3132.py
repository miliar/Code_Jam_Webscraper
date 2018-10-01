def flip(digits, index):
    digits[index] -= 1
    for i in range(index+1, len(digits)):
        digits[i] = 9


numcases = int(input())

for i in range(numcases):
    digits = list(map(int, list(input())))

    for j in range(len(digits) - 2, -1, -1):
        if digits[j] > digits[j+1]:
            flip(digits, j)

    print('Case #' + str(i+1) + ':', ''.join(map(str,digits)).lstrip('0'))

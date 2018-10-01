loops = range(1, int(raw_input()) + 1)
for loop in loops:
    number = int(raw_input())
    digits = [int(i) for i in str(number)]
    while True:
        for index, (i, j) in enumerate(zip(digits, digits[1:])):
            if j < i:
                for prev_digit in range(index, -1, -1):
                    if digits[prev_digit] != 0:
                        digits[prev_digit] -= 1
                        break
                for next_digit in range(prev_digit + 1, len(digits)):
                    digits[next_digit] = 9
                break
        else:
            answer = 0
            for place, digit in enumerate(digits[::-1]):
                answer += digit * (10 ** place)
            print "Case #{}: {}".format(loop, answer)
            break

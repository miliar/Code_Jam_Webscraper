def fix_tidy_number(numbers: [int]) -> [int]:
    num_digits = len(numbers)
    if num_digits == 1:
        return [numbers[0] - 1]
    else:
        # Check for tidyness
        last_number = numbers[num_digits - 1]
        new_last_number = last_number - 1
        next_to_last_number = numbers[num_digits - 2]
        if new_last_number < next_to_last_number:
            return fix_tidy_number(numbers[:num_digits - 1]) + [9]
        else:
            numbers[num_digits - 1] = new_last_number
            return numbers


t = int(input())

for i in range(1, t+1):
    n = input()
    tidy_numbers = []
    fixed_numbers = []
    previous_digit = -1
    for index, digit in enumerate(map(lambda x: int(x), n)):
        if index == 0:
            previous_digit = digit
            tidy_numbers.append(digit)
            continue

        if digit >= previous_digit:
            previous_digit = digit
            tidy_numbers.append(digit)
        else:
            # We found a bad number
            # print(f"We found a bad number! {digit}")
            # Fix the ones we have and then
            tidy_numbers = fix_tidy_number(tidy_numbers) + [9] * (len(n) - index)
            break
    last_tidy_number = int(''.join(map(str, tidy_numbers)))
    print(f"Case #{i}: {last_tidy_number}")

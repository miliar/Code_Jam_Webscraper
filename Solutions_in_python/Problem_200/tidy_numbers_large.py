import simonsolver

simon = simonsolver.SimonSolver('tidy_numbers_large.txt')
practice_input = simon.read_file('./tidy_numbers_input_large.txt')

CASES = int(practice_input[0])

outputs = []


def get_tidy(num):
    num = list(num)
    l = len(num)

    for i, n in enumerate(num):
        if i == (l - 1):
            break

        next = num[i + 1]

        if int(n) > int(next):
            n = int(n) - 1
            new_num = num[0:i]
            new_num.append(str(n))
            new_num.append(('9' * (l - len(new_num))))
            if new_num[0] == '0':
                new_num = new_num[1:]
            return get_tidy(''.join(new_num))

    return ''.join(num)

simon.start()
for case in practice_input[1:-1]:
    num = case

    if int(num) < 10:
        outputs.append(num)
        continue

    tidy = get_tidy(num)
    outputs.append(tidy)
    foo = 'bar'

simon.end()
simon.output_with_case_numbers(outputs)
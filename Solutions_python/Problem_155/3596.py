__author__ = 'liraim'


def read_line(fd):
    split_string = fd.readline().split()
    maximum_shyness = int(split_string[0])
    shy_people_count = [int(c) for c in split_string[1]]
    return maximum_shyness, shy_people_count


def read_input(fd):
    test_count = int(fd.readline())
    tests = [(i, read_line(fd)) for i in range(1, test_count + 1)]
    return tests


def solve_test(i, input_val):
    count, shy_people_count = input_val
    current_amount = 0
    current_shyness = 0
    additional_guests = 0
    for count in shy_people_count:
        if count > 0:
            if current_amount < current_shyness:
                additional_guests += (current_shyness - current_amount)
                current_amount += additional_guests
            current_amount += count
        current_shyness += 1
    return i, additional_guests


def solve(tests):
    answers = [solve_test(i, test) for i, test in tests]
    return answers


def output_answer(answers, fd):
    for answer in answers:
        fd.write("Case #{0}: {1}\n".format(answer[0], answer[1]))


fd_in = open('A-small-attempt2.in')
fd_out = open('result2.out', 'w')
output_answer(solve(read_input(fd_in)), fd_out)
fd_in.close()
fd_out.close()


# -*- coding: utf-8 -*-
# !python3

__author__ = 'lostcoaster'


class InputFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.test_count = 0

    def __iter__(self):
        with open(self.filename) as file:
            self.test_count = int(file.readline().strip())
            for test_i in range(1, self.test_count+1):
                count, audiences = file.readline().strip().split(' ')
                audiences = list(int(i) for i in audiences)  # split into numbers
                yield (count, audiences)


class AnswerFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.case_num = 0

    def put(self, answer):
        self.case_num += 1
        with open(self.filename, 'a') as file:
            to_write = 'Case #{}: {}\n'.format(self.case_num, str(answer))
            print(to_write)
            file.write(to_write)


def solve(audiences):
    friends = 0
    counter = 0
    for i in range(len(audiences)-1):  # the last count is irrelevant
        counter += audiences[i]
        friends = max(i+1-counter, friends)  # friends must be enough to activate the next batch
    return friends


if __name__ == '__main__':
    input_file = InputFile('a_b.in')
    answers = AnswerFile('a_b.out')
    for data in input_file:
        answers.put(solve(data[1]))
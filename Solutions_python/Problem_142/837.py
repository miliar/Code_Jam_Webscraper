import unittest
import sys
from collections import deque


def getProblemAnswer(n, strings):
    lengths = [len(s) for s in strings]
    pointers = [-lengths[i] - 1 for i in range(n)]
    total = 0
    firsts = set([s[0] for s in strings])
    lasts = set([s[-1] for s in strings])
    if len(firsts) > 1 or len(lasts) > 1:
        return 'Fegla Won'

    while pointers[0] < -1:
        cur_letter = strings[0][pointers[0] + 1]
        try:
            moove_to_next(n, cur_letter, strings, pointers, lengths)
            diffs = num_letters(n, cur_letter, strings, pointers, lengths)
            total += process_diff(n, diffs)
        except:
            return 'Fegla Won'
        try:
            while strings[0][pointers[0] + 1] == cur_letter and pointers[0] < -1:
                pointers[0] += 1
                diffs[0] += 1
        except:
            break
    for p in pointers:
        if p != -1:
            return 'Fegla Won'
    return total


def moove_to_next(n, cur_letter, strings, pointers, lengths):
    for i in range(n):
        pointers[i] += 1
        while strings[i][pointers[i]] is not cur_letter:
            pointers[i] += 1


def num_letters(n, cur_letter, strings, pointers, lengths):
    diffs = [0 for s in strings]
    for i in range(n):
        try:
            while strings[i][pointers[i] + 1] is cur_letter and pointers[i] < -1:
                pointers[i] += 1
                diffs[i] += 1
        except:
            pass
    return diffs


def process_diff(n, diffs):
    mintotal = 100*100
    for i in range(min(diffs), max(diffs) + 1):
        vals = [max(d - i, i - d) for d in diffs]
        total = int(sum(vals))
        if mintotal > total:
            mintotal = total
    return mintotal


class Tests(unittest.TestCase):

    def test_unit(self):
        self.assertEqual(getProblemAnswer(3, ['abc', 'abc', 'aaaaabc']), 4)
        self.assertEqual(getProblemAnswer(2, ['jgvljefwqjd', 'tjgvljefwqjd']), 'Fegla Won')
        self.assertEqual(getProblemAnswer(2, ['aaa', 'aaa']), 0)
        self.assertEqual(getProblemAnswer(2, ['gcj', 'cj']), 'Fegla Won')
        self.assertEqual(getProblemAnswer(2, ['gccj', 'ccj']), 'Fegla Won')
        self.assertEqual(getProblemAnswer(2, ['cj', 'cjg']), 'Fegla Won')
        self.assertEqual(getProblemAnswer(2, ['mmaw', 'mmaw']), 0)
        self.assertEqual(getProblemAnswer(2, ['maw', 'mmaw']), 1)
        self.assertEqual(getProblemAnswer(2, ['mmaw', 'maw']), 1)
        self.assertEqual(getProblemAnswer(3, ['aabc', 'abbc', 'abcc']), 3)
        self.assertEqual(getProblemAnswer(2, 
            ['xxcekmnnczqvfbjhyysjexeeerfjjjotiifppqvmsbwgpaaifynghuhgosmlxgtguoqbegwqaypjnprunedxakfpc',
            'xcekmnczqvfbjhyysjexerfjotifpqvmsbwgpaifynghuhgosmlxgtguoqbegwqaypjnprunedxakfpc']),
        9)

    def test_sample(self):
        path = 'a'
        f = open(path + '.out')
        lines = f.readlines()
        f.close()
        f = open(path + '.expected.out')
        expected_lines = f.readlines()
        f.close()
        # self.assertEqual(lines, expected_lines)


def main(arg1):
    print 'opening ' + arg1
    f = open(arg1 + '.in')
    lines = f.readlines()
    f.close()
    lines = deque([case[:-1] for case in lines])
    #print [case for case in lines]
    number_test_cases = int(lines.popleft())
    print 'a total of ' + str(number_test_cases) + ' cases'

    output = []

    for case_number in range(number_test_cases):
        n = int(lines.popleft())
        strings = []
        for i in range(n):
            strings.append(lines.popleft())

        result = getProblemAnswer(n, strings)
        output.append('Case #' + str(case_number + 1) + ': %s' % result)
    output = '\n'.join(output)

    should_write = False
    should_write = True
    if should_write:
        write_answer(arg1 + '.out', output)
    else:
        print 'NOT WRITING ANYTHING \n'


def write_answer(name, output):
    f = open(name, 'w+')
    f.write(output)
    f.close()
    print 'ANSWERS WRITTEN\n'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        sys.exit(main(sys.argv[1]))
    else:
        unittest.main()

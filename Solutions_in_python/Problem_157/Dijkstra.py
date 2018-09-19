#!/usr/bin/python
# -*- coding: utf-8 -*-

times_table = {
    '11': '1',
    '1i': 'i',
    '1j': 'j',
    '1k': 'k',
    'i1': 'i',
    'ii': '-1',
    'ij': 'k',
    'ik': '-j',
    'j1': 'j',
    'ji': '-k',
    'jj': '-1',
    'jk': 'i',
    'k1': 'k',
    'ki': 'j',
    'kj': '-i',
    'kk': '-1',
    '-11': '-1',
    '-1i': '-i',
    '-1j': '-j',
    '-1k': '-k',
    '-i1': '-i',
    '-ii': '1',
    '-ij': '-k',
    '-ik': 'j',
    '-j1': '-j',
    '-ji': 'k',
    '-jj': '1',
    '-jk': '-i',
    '-k1': '-k',
    '-ki': '-j',
    '-kj': 'i',
    '-kk': '1'
}

if __name__ == '__main__':
    with open('C-small-attempt1.in') as problem_input:
        with open('C-small.out', 'w') as problem_output:
            test_cases = int(problem_input.readline().strip())

            for test_case in xrange(test_cases):
                _, reps = problem_input.readline().strip().split()
                misspelled = list(problem_input.readline().strip()) * int(reps)
                i_found, j_found, k_found = False, False, False

                left_op = misspelled[0]

                if left_op == 'i':
                    i_found = True

                for index, right_op in enumerate(misspelled[1:]):
                    left_op = times_table[left_op + right_op]
                    if left_op == 'i':
                        i_found = True
                    if i_found and left_op == 'k':
                        j_found = True
                    if j_found and left_op == '-1' and index + 1 == len(misspelled) - 1:
                        k_found = True


                points_back = 'YES' if i_found and j_found and k_found else 'NO'

                output = 'Case #{0}: {1}\n'.format(test_case + 1, points_back)

                #print output.strip()
                problem_output.write(output)
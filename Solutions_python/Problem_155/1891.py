#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('A-small-attempt2.in') as problem_input:
        with open('A-small.out', 'w') as problem_output:
            test_cases = int(problem_input.readline().strip())

            for test_case in xrange(test_cases):
                _, shyness_cnts = problem_input.readline().strip().split()
                standing, need_standing = 0, 0

                for shyness, cnt in enumerate(shyness_cnts):
                    cnt = int(cnt)

                    if shyness == 0:
                        standing += cnt
                    else:
                        if cnt == 0 or standing >= shyness:
                            standing += cnt
                        else:
                            need_standing += (shyness - standing)
                            standing += (need_standing + cnt)

                output = 'Case #{0}: {1}\n'.format(test_case + 1, need_standing)

                problem_output.write(output)
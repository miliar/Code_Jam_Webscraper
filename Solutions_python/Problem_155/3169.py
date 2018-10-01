#/usr/bin/env/python

import sys


def _standing_ovation(n_shynesses, audience, case_num):
    additional = 0
    cumul_audience = [sum(audience[0:i]) for i in range(n_shynesses + 1)]

    for (shyness, standing) in zip(range(n_shynesses), cumul_audience):
        standing_eff = standing + additional
        if standing_eff < shyness:
            additional += shyness - standing_eff

    print 'Case #{case_num}: {addl}'.format(case_num=case_num, addl=additional)


def _parse_case_line(case_line):
    s_max, audience = case_line.strip().split()
    n_shys, audience = int(s_max) + 1, [int(group) for group in audience]
    return n_shys, audience


def _test_cases(filename):
    with open(filename, 'rb') as f:
        n_cases = int(f.readline().strip())

        for i in range(n_cases):
            n_shynesses, audience = _parse_case_line(f.readline())
            _standing_ovation(n_shynesses, audience, case_num=(i + 1))


def main():
    filename = sys.argv[1]
    _test_cases(filename)


if __name__ == "__main__":
    main()

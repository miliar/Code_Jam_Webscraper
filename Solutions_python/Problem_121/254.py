import os

PROB_NAME = 'energy'
INPUT_TYPE = 'small4'


def first_idx(seq, pred):
    for idx, item in enumerate(seq):
        if pred(item):
            return idx


def solve(case):
    """break 'case', solve and return the solution"""
    e, r, n, v = case
    max_e = e
    total_gain = 0

    if r >= e:
        return sum(gain * e for gain in v)

    l = False
    for i, gain in enumerate(v):
        if i < n - 1 and max(v[i + 1:]) > gain:
            m = max(v[i + 1:])
            next_idx = first_idx(v[i + 1:], lambda x: x > gain) + i + 1
            x = max((next_idx - i) * r - (max_e - e), 0)
            e += r - x
            total_gain += gain * x
        else:
            total_gain += e * gain
            e = r

    return total_gain


def read_file(filepath):
    """Read the input file and return a list of cases in a tuple format."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for case in range(num_cases):
            # read each case here
            e, r, n = [int(num) for num in lines.pop(0).split()]
            v = [int(num) for num in lines.pop(0).split()]
            cases.append((e, r, n, v))
    return cases


def write_results(results, outfile):
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


def main(infile, outfile):
    cases = read_file(infile)
    results = [solve(case) for case in cases]
    write_results(results, outfile)

main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
     os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))

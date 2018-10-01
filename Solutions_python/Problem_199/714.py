# problem 1
import sys
sys.path.append('/Users/jakemagner/Desktop/google_code_jam/year_2017/')
from random import randint
from util.io import get_only_file_in_downloads


def solve_bits(bits, k):
    # left to right
    # flip at first 0 bit then continue
    flips = 0
    for i in xrange(len(bits) - k + 1):
        if bits[i] == 0:
            flips += 1
            for j in xrange(i, i + k):
                bits[j] = 1 - bits[j]
    if sum(bits) == len(bits):
        return flips
    return None


def random_bits(n):
    return [randint(0, 1) for x in xrange(n)]


def flip_random_bit(bits, k):
    ind = randint(0, len(bits) - k)
    for i in xrange(ind, ind + k):
        bits[i] = '+' if bits[i] == '-' else '-'
    return ind


def generate_problems(T, S):
    for case in xrange(T):
        s = randint(2, S)
        k = randint(2, s)
        bits = ['+'] * s
        num_flips = randint(1, S - 1)
        inds = []
        for i in xrange(num_flips):
            inds.append(flip_random_bit(bits, k))
        if randint(0, 2) == 0:  # flip a bit to make some impossible
            flip_random_bit(bits, 1)
            num_flips = None
        yield ''.join(bits), k, num_flips, inds


def generate_input(T, S, target_file):
    target_file.write('%d\n' % T)
    answers_file = open('answers.txt', 'w')
    i = 1
    for bits, k, num_flips, inds in generate_problems(T, S):
        target_file.write('%s %d\n' % (bits, k))
        answers_file.write('Case #%d: %s\t' % (i, str(num_flips) if num_flips else 'IMPOSSIBLE'))
        answers_file.write('%s\n' % ','.join([str(x) for x in inds]))
        i += 1
    target_file.close()
    answers_file.close()


def solve_problemA_input_line(line):
    bits, k = line.split(' ')
    int_bits = [0 if x == '-' else 1 for x in bits]
    answer = solve_bits(int_bits, int(k.strip()))
    return answer


def generate_output(input_file):
    num_cases = None
    for i, line in enumerate(input_file):
        if i == 0:
            num_cases = int(line.strip())
            continue
        if i > num_cases:
            break
        answer = solve_problemA_input_line(line)
        if answer is None:
            print 'Case #%d: IMPOSSIBLE' % i
        else:
            print 'Case #%d: %d' % (i, answer)




if __name__ == '__main__':
    path = None
    if len(sys.argv) == 2:
        path = sys.argv[1]
    if path is None:
        input_file = get_only_file_in_downloads()
    else:
        input_file = open(path)
    generate_output(input_file)

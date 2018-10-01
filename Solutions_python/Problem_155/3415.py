import sys

DEBUG = True


def solver(input_string):
    input_string = input_string.strip()
    debug(input_string)
    shynesses = [int(c) for c in input_string if c]
    standing = 0
    additions = 0
    for idx, count in enumerate(shynesses):
        if idx <= standing:
            standing += count
        else:
            additions += idx - standing
            standing += (idx - standing) + count
    return additions


def ssi(s, func=int):
    """
    space separated integers
    """
    return map(func, s.strip('\n').split())


def rl():
    return sys.stdin.readline()


def debug(*args):
    if args[-1] is not False and DEBUG:
        msg = " ".join([str(m) for m in args])
        sys.stderr.write(msg + '\n')


def main():
    # open input file
    # input_file = open('infile.txt')

    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        debug('Case #%d' % (c + 1))
        answer = solver(rl().split(" ")[1])
        output.append('Case #%d: %s\n' % (c + 1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()


if __name__ == '__main__':
    main()

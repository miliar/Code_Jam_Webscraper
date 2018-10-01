import sys
import random
import copy


def make_problem(num):
    result = []
    print result
    return result


def read_data(input):
    R, C, W = map(int, input.readline().strip().split())
    return R, C, W


def small_solution(R, C, W):
    result = 0

    currentPos = 0
    delta = 0
    for i in range(C):
        currentPos += W
        result += 1
        delta = C - currentPos
        if delta <= W:
            break

    print delta, result
    if R != 1:
        tmp = (result + 1) * (R - 1)
        result += tmp


    if currentPos == C:
        result += W - 1
    else:
        result += W

    return str(result)


def large_solution(size, data):
    result = 0
    return str(result)


if __name__ == '__main__':
    input_stream = open(sys.argv[0].replace('.py', '') + '.in', 'r')
    output_stream = open(sys.argv[0].replace('.py', '') + '.out', 'w')

    T = int(input_stream.readline().strip())
    for caseN in range(1, T + 1):
        print 'Case #%i: calculation' % (caseN)
        result = small_solution(*read_data(input_stream))
        # result = large_solution(read_data(input_stream))
        out_line = 'Case #%i: %s\n' % (caseN, result)
        output_stream.write(out_line)
        output_stream.flush()

    input_stream.close()
    output_stream.close()


# [i for i in range(5) if i > 2]
# a,b = b,a
# print True if a > 4 else False

import sys

SIZE = 4

def get_indexes(i, j, size=SIZE):
    result = []
    result.append(j)
    result.append(i + size)
    if i == j:
        result.append(size+size)
    if i + j + 1 == size:
        result.append(size+size + 1)
    return result

def make_work(input='input.txt', output='output.txt'):
    file_in = open(input)
    cases_number = int(file_in.readline().strip())
    for n in xrange(cases_number):
        result = [0 for i in xrange(SIZE+SIZE+2)]
        has_t = [False for i in xrange(SIZE+SIZE+2)]
        point_count = 0
        for i in xrange(SIZE):
            line = file_in.readline().strip()
            for j, v in enumerate(line):
                indexes = get_indexes(i, j)
                if v == '.':
                    point_count += 1
                elif v == 'T':
                    for index in indexes:
                        has_t[index] = True
                elif v == 'X':
                    for index in indexes:
                        result[index] += 1
                elif v == 'O':
                    for index in indexes:
                        result[index] -= 1
        file_in.readline()
        
        for r, t in enumerate(has_t):
            if t: 
                if result[r] > 0:
                    result[r] += 1
                if result[r] < 0:
                    result[r] -= 1
        x_win = False
        o_win = False
        for x in result:
            if x == 4:
                x_win = True
            if x == -4:
                o_win = True

        case_number = n + 1
        if x_win:
            print "Case #%s: X won" % case_number
        elif o_win:
            print "Case #%s: O won" % case_number
        elif point_count == 0:
            print "Case #%s: Draw" % case_number
        else:
            print "Case #%s: Game has not completed" % case_number
        


if len(sys.argv) >= 2:
    make_work(input=sys.argv[1])
else:
    make_work()

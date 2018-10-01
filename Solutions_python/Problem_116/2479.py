import sys
import logging
import os.path

def setup_logging():
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    console.setFormatter(formatter)

    logger = logging.getLogger('flood')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console)

setup_logging()
logger = logging.getLogger('flood')


def solve(a):

    b = [[0 for i in range(4)] for l in range(4)]
    c = [[0 for i in range(4)] for l in range(4)]

    for x in range(4):
        for y in range(4):
            b[x][y] = a[x][y]
            c[x][y] = a[y][x]

    draw = True
    for x in range(4):
        last = None
        for y in range(4):
            if b[x][y] == '.':
                draw = False
                break
            elif b[x][y] == 'T':
                if y == 3:
                    return last
                continue
            elif not last:
                last = b[x][y]
            elif last != b[x][y]:
                break
            if y == 3:
                return last
    draw = True
    for x in range(4):
        last = None
        for y in range(4):
            if c[x][y] == '.':
                draw = False
                break
            elif c[x][y] == 'T':
                if y == 3:
                    return last
                continue
            elif not last:
                last = c[x][y]
            elif last != c[x][y]:
                break
            if y == 3:
                return last

    last = None
    for x in range(4):
        if a[x][x] == '.':
            break
        if a[x][x] == 'T':
            if x == 3:
                return last
            continue
        if not last:
            last = a[x][x]
            continue
        if a[x][x] != last:
            break
        if x == 3:
            return last

    last = None
    for x in range(4):
        if a[x][3-x] == '.':
            break
        if a[x][3-x] == 'T':
            if x == 3:
                return last
            continue
        if not last:
            last = a[x][3-x]
            continue
        if a[x][3-x] != last:
            break
        if x == 3:
            return last
            logger.debug("HERE")
    
    return draw



            

if __name__ == "__main__":

    input_file = sys.argv[1]
    logger.info(input_file)

    if not os.path.isfile(input_file):
        logger.error("%s not a file" % input_file)
        sys.exit(1)

    fh = open(input_file, 'r')
    num_test_cases = int(fh.readline().strip())
    logger.debug("%s test cases" % num_test_cases)


    result = {'X': 'X won',
              'O': 'O won',
              True: 'Draw',
              False: 'Game has not completed'}

    for test_case in range(num_test_cases):
        case_string = "Case #%s:" % (test_case + 1)
        logger.debug(case_string)
        a = []
        a.append(fh.readline().strip())
        a.append(fh.readline().strip())
        a.append(fh.readline().strip())
        a.append(fh.readline().strip())


        
        logger.debug("array_1: %s" % a[0])
        logger.debug("array_2: %s" % a[1])
        logger.debug("array_3: %s" % a[2])
        logger.debug("array_4: %s" % a[3])
        logger.debug(a)

        print "%s %s" % (case_string, result[solve(a)] )
        fh.readline()
        
    fh.close() 


import copy
import sys
from pprint import pprint
from copy import deepcopy
import math

input = file(sys.argv[1])
testcases = int(input.readline())
testcase = 1

if __name__ == '__main__':
    try:
        while testcase <= testcases:
            good, participants, factor = map(int, input.readline().split())
            x = good
            count = 0
            while x < participants:
                x = (x) * factor
                count += 1
            log = int(math.log(count, 2))
            if 2 ** int(log) != count:
                log += 1
            result = str(log)
            print 'Case #%i: %s' % (testcase, result)
            testcase += 1
    except:
        import pdb;pdb.post_mortem()

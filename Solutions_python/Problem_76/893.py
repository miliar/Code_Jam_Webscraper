import sys
import os
import itertools

path = os.path.abspath(sys.argv[1])
with open(path) as test_file:
    t = int(test_file.readline().strip())
    i = 1
    while t > 0:
        n = int(test_file.readline().strip())
        input_case = test_file.readline().strip().split()
        input_case = list(int(e) for e in input_case)
        input_sum = sum(input_case)
        input_set = []
        for m in range(1, len(input_case) / 2 + 1):
            input_set.extend(list(itertools.combinations(input_case, m)))
       
        min_half = input_sum
        stop = False
        for e in input_set:
            r = []
            r.extend(input_case)
            for ee in e:
                r.remove(ee)
            af = reduce(lambda x, y : x ^ y, e)
            bf = reduce(lambda x, y : x ^ y, r)
            ar = reduce(lambda x, y : x + y, e)
            br = reduce(lambda x, y : x + y, r)
            if af == bf and af > 0:
                stop = True
                if ar < min_half:
                    min_half = ar
                if br < min_half:
                    min_half = br
        print 'Case #%d: %s' % (i, str(input_sum - min_half) if stop else 'NO')
        t -= 1
        i += 1
    

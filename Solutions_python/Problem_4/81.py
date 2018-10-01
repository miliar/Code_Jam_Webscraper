import sys, operator
data = filter(None, map(lambda x:x.strip(), open(sys.argv[1]).readlines()))

def pop_int(data):
    return int(data.pop(0))

def pop_ints(data):
    return map(int, data.pop(0).split())

def pop_rows(data, num_rows):
    result = data[:num_rows]
    for i in range(num_rows):
        data.pop(0)
    return result

def pop_case(data):
    length = pop_int(data)
    v1 = pop_ints(data)
    v2 = pop_ints(data)
    return length, v1, v2

def scalar_product(v1, v2):
    return sum(map(operator.mul, v1, v2))
     
num_cases = pop_int(data)
for case_num in range(1, num_cases+1):
    length, v1, v2 = pop_case(data)
    v1.sort()
    v2.sort()
    v2.reverse()
    print "Case #%d: %d" % (case_num, scalar_product(v1, v2))

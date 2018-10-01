import operator
import sys


def solve(n, tn, probs):
    antiprobs = [1 - p for p in probs]
    succ = reduce(operator.__mul__, probs, 1)
    expp = []
    expp.append( (tn - n + 1) * succ + (tn + tn - n + 2) * (1 - succ) )
    
    for i, p in enumerate(probs):
        _i = (i + 1)
        pri = (n - _i)
        succ_i = reduce(operator.__mul__, probs[:pri], 1)
        succ_ks = (tn - n + 1 + 2 * _i)
        fail_i = 1 - succ_i
        fail_ks = succ_ks + tn + 1 
        if _i != n:
            expp.append(succ_i * succ_ks + fail_i * fail_ks)
        else:
            expp.append(1 * succ_ks)

    if n == tn:
        expp.append( succ * 1 + (1 - succ) * (tn + 2) )
    else:
        expp.append( tn + 2 )

    return min(expp)

def main(input_filename, output_filename):
    
    input_f = open(input_filename, "r")
    output_f = open(output_filename, "w")
    
    try:
        TEST_CASES_NUM = int(input_f.readline())
        
        for test_case_i in xrange(TEST_CASES_NUM):

            # print test_case_i
            
            inp = [int(_) for _ in input_f.readline().strip().split(' ')]
            n, tn = inp[0], inp[1]
            probs = [float(_) for _ in input_f.readline().strip().split(' ')]
            
            res = solve(n, tn, probs)
            output_f.write("Case #%d: %.6f\n" % (test_case_i + 1, res))
            
    finally:
        input_f.close()
        output_f.close()


main(sys.argv[1], sys.argv[2])

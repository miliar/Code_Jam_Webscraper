
PROBLEM_ID = "C" # A B or C
PROBLEM_SIZE = "small"

def run():
    """I/O handler"""
    file_name = "{}-{}".format(PROBLEM_ID, PROBLEM_SIZE)
    in_f = open('{}.txt'.format(file_name), 'r')
    out_f = open('{}.out'.format(file_name), 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)

def solve_case(in_f, out_f, case_index):
    """problem solver"""
    print "case #{}:".format(case_index)
    A, B, K = map(int, in_f.readline().rstrip('\n').split())
    
    ss = 0
    for x in xrange(A):
        for y in xrange(B):
            if x&y < K:
                ss += 1
    
    # get the solution 

    # write the solution   
    print A, B, K, ss
    out_f.write("Case #{}: {}\n".format(case_index, ss))

run()


in_file = "B-small-attempt0.in"
out_file = "b.out"
out = open(out_file, 'w')

    
def lottery(A, B, K):
    result = 0
    for a in range(A):
        for b in range(B):
            if a&b < K:
                result += 1
    return result 

def result_out(case, result):
    out.write("Case #" + str(case) + ": " + str(result) + '\n')

with open(in_file) as f:
    case_num = int(f.readline())

    for case in range(1, case_num + 1):
        line = f.readline().strip().split(' ')
        A = int(line[0])
        B = int(line[1])
        K = int(line[2])
        result = lottery(A, B ,K)
        result_out(case, result)




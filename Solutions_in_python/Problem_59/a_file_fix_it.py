def parse(line):
    current_dir = dirs
    result = 0
    for dir in line:
        if not dir in current_dir:
            current_dir[dir] = {}
            result += 1
        current_dir = current_dir[dir]
    return result

input_file=open('E:\A-large.in', 'r')
output_file=open('A-large.out', 'w')

test_cases=int(input_file.readline())

for case_num in range(1, test_cases+1):
    dirs = {}
    case=input_file.readline().split()
    N, M = map(int, case)
    #print N, M
    num_mkdir = 0
    for i in range(N):
        line = input_file.readline().strip().split("/")
        del line[0]
        parse(line)
        #print dirs, num_mkdir
    for i in range(M):
        line = input_file.readline().strip().split("/")
        del line[0]
        num_mkdir += parse(line)
        #print dirs, num_mkdir
    output_file.write("Case #%s: %s\n" %(case_num, num_mkdir))
    
output_file.close()

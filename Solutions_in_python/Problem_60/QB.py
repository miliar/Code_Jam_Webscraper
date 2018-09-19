#! /usr/bin/env python
#coding=utf-8


def solve(icase, case_input):
    case_output = 'Case #%d: '%icase
    
#    print icase, case_input
    N, K, B, T = [int(x) for x in case_input[0].split()]
    xx = [int(x) for x in case_input[1].split()]
    vv = [int(x) for x in case_input[2].split()]
    pp = [(xx[i] + T * vv[i] >= B) for i in xrange(N)]
    if pp.count(True) < K:
        case_output += 'IMPOSSIBLE'
        return case_output
    pp.reverse()
    count = 0
    idx = -1
    for i in xrange(K):
        idx = pp.index(True, idx + 1)
        count += idx - i
        
    case_output += '%d'%count
    
    return case_output  


def main():
    global use_test_data
    global test_data
    global input_file
    global output_file
    
    if use_test_data:
        data = [x.strip() for x in test_data.split('\n')]
    else:
        data = [x.strip() for x in input_file.readlines()]
    
    T = int(data[0])
    iLine = 1
    caseLineNum = 3
    for icase in range(1, T + 1):
        input = []
#        N, K = [int(x) for x in data[iLine].split()]
#        caseLineNum = N + K
#        input.append(data[iLine])
#        iLine += 1
        for i in range(caseLineNum):
            input.append(data[iLine])
            iLine += 1
        rslt = solve(icase, input)
        print rslt
        if not use_test_data:
            print >> output_file, rslt
    
    if not use_test_data:
        input_file.close()
        output_file.close()
    
    
if __name__ == '__main__':
    test_data = """3
5 3 10 5
0 2 5 6 7
1 1 1 1 4
5 3 10 5
0 2 3 5 7
2 1 1 1 4
5 3 10 5
0 2 3 4 7
2 1 1 1 4"""
    use_test_data = False
    
    test_file = 'B-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()
    
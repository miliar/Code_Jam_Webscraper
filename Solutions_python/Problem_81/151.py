#! /usr/bin/env python
#coding=utf-8

def solve(icase, case_input):
#    for _d in case_input:
#        print _d
    case_output = 'Case #%i: '%icase

    N = int(case_input[0])
    mm = case_input[1:]
    w = []
    t = []
    for i in xrange(N):
        w.append(mm[i].count('1'))
        t.append(w[i]+mm[i].count('0'))
    wp = []
    owp = []
    oowp = []
    for i in xrange(N):
        wp.append(1.*w[i]/t[i])
    for i in xrange(N):
        s = 0
        for ii in xrange(N):
            if mm[i][ii] == '1':
                s += 1.*w[ii]/(t[ii] - 1)
            elif mm[i][ii] == '0':
                s += 1.*(w[ii]-1)/(t[ii] - 1)
        owp.append(s/t[i])
    for i in xrange(N):
        s = 0
        for ii in xrange(N):
            if mm[i][ii] != '.':
                s += owp[ii]
        oowp.append(s/t[i])
    for i in xrange(N):
        rpi = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]
        case_output += '\n%.7f'%rpi
    
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
    caseLineNum = 1
    for icase in range(1, T + 1):
        caseLineNum = int(data[iLine]) + 1
        input = []
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
    test_data = """2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.
    """
    use_test_data = False
    
    test_file = 'A-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()
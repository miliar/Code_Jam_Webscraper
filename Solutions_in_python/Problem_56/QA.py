#! /usr/bin/env python
#coding=utf-8


def coding(key, line):
    rslt = 0
    for c in line:
        rslt = rslt << 1
        rslt += c == key and 1 or 0
    return rslt


def row_win(kk, vv):
    for v in vv:
        count = 0
        while v != 0:
            t = v & 1
            v = v >> 1
            if t == 1:
                count += 1
            else:
                count = 0
            if count == kk:
                return True
    return False


def colum_win(kk, vv):
    for i in xrange(len(vv) - kk + 1):
        if vv[i] != 0:
            t = reduce(lambda x, y: x & y, vv[i:i+kk])
            if 0 != t:
                return True
    return False


def diag1_win(kk, vv):
    for i in xrange(len(vv) - kk + 1):
        if vv[i] != 0:
            t = vv[i]
            for j in xrange(kk):
                t &= vv[i + j] >> j
                if t == 0:
                    break
            else:
                return True
    return False

    
def diag2_win(kk, vv):
    for i in xrange(len(vv) - kk + 1):
        if vv[i] != 0:
            t = vv[i]
            for j in xrange(kk):
                t &= vv[i + j] << j
                if t == 0:
                    break
            else:
                return True
    return False


def solve(icase, case_input):
    case_output = 'Case #%d: '%icase
    
#    print icase, case_input
    N, K = [int(x) for x in case_input[0].split()]
    rt = [line.replace('.', '') for line in case_input[1:]]
    rcodes = [coding('R', line) for line in rt]
    bcodes = [coding('B', line) for line in rt]
    
    winc = 0
    if row_win(K, rcodes) or colum_win(K, rcodes) or diag1_win(K, rcodes) or diag2_win(K, rcodes):
        winc |= 1
    if row_win(K, bcodes) or colum_win(K, bcodes) or diag1_win(K, bcodes) or diag2_win(K, bcodes):
        winc |= 2
        
    if winc == 0:
        case_output += 'Neither'
    elif winc == 1:
        case_output += 'Red'
    elif winc == 2:
        case_output += 'Blue'
    elif winc == 3:
        case_output += 'Both'
    else:
        raise "WRONG"
    
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
    caseLineNum = 2
    for icase in range(1, T + 1):
        input = []
        N, K = [int(x) for x in data[iLine].split()]
        caseLineNum = N
        input.append(data[iLine])
        iLine += 1
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
    test_data = """4
7 3
.......
.......
.......
...R...
...BB..
..BRB..
.RRBR..
6 4
......
......
.R...R
.R..BB
.R.RBR
RB.BBB
4 4
R...
BR..
BR..
BR..
3 3
B..
RB.
RB."""
    use_test_data = False
    
    test_file = 'A-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()
    
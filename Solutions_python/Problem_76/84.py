# -*- coding: utf-8 -*-

INPUT_FILE_PATH = "C-large-975485.in"
OUTPUT_FILE_PATH = "C-large-975485.out"

fr = open(INPUT_FILE_PATH, 'r')
fw = open(OUTPUT_FILE_PATH, 'w')

T = int(fr.readline().strip())

def bin_calc(op1, op2):
    # op1 = 10, op2 = 6
    # a = '1010', b = '110'
    a = format(op1, 'b')
    b = format(op2, 'b')
    
    a_len = len(a)
    b_len = len(b)

    if a_len < b_len:
        tmp = b_len - a_len
        for i in range(tmp):
            a = '0' + a
    else:
        tmp = a_len - b_len
        for i in range(tmp):
            b = '0' + b

    # a = '1010', b = '0110'
    ret = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ret += '0'
        else:
            ret += '1'
    ret = int(ret, 2)
    return ret

for i in range(T):
    N = int(fr.readline().strip())
    C_LIST = fr.readline().strip().split()
    tmp_c_list = []
    for j in range(N):
        tmp = C_LIST[j]
        tmp_c_list.append(int(tmp))

    for j in range(N - 1):
        op1 = tmp_c_list.pop(0)
        op2 = tmp_c_list.pop(0)
        ret = bin_calc(op1, op2)
        tmp_c_list.append(ret)

    if tmp_c_list[0] == 0:
        min = 1000000
        sum = 0
        for j in range(N):
            tmp = int(C_LIST.pop(0))
            sum += tmp
            if tmp < min:
                min = tmp
        sum -= min
        fw.write("Case #%d: %d\n" % (i + 1, sum))
        print sum
    else:
        fw.write("Case #%d: NO\n" % (i + 1))
        print "NO"

    # write result 


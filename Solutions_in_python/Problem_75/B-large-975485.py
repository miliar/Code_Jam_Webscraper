# -*- coding: utf-8 -*-

INPUT_FILE_PATH = "B-large-975485.in"
OUTPUT_FILE_PATH = "B-large-975485.out"

fr = open(INPUT_FILE_PATH, 'r')
fw = open(OUTPUT_FILE_PATH, 'w')

T = int(fr.readline().strip())

for i in range(T):
    tmp_list = fr.readline().strip().split()
    C = int(tmp_list.pop(0))
    C_LIST = []
    for j in range(C):
        C_LIST.append(tmp_list.pop(0))
    D = int(tmp_list.pop(0))
    D_LIST = []
    for j in range(D):
        D_LIST.append(tmp_list.pop(0))


    N = int(tmp_list.pop(0))
    N_STRING = tmp_list.pop(0)
    
    result = []

    for j in range(len(N_STRING)):
        # result = ['A', 'E', 'Q', ...]
        result.append(N_STRING[j])

        # for combine
        for c in C_LIST:
            # c = "QR->T"
            if len(result) >= 2:
                if result[-1] == c[0] and result[-2] == c[1] or result[-1] == c[1] and result[-2] == c[0]:
                    result.pop(-1)
                    result.pop(-1)
                    result.append(c[2])
                
        # for opposed
        for d in D_LIST:
            # d = "QR"
            if len(result) >= 2:
                if d[0] in result and d[1] in result:
                    result = []

    print result
    tmp = "Case #%d: [" % (i + 1)
    for r in result:
        tmp += "%c, " % r
    if result:
        tmp = tmp[:-2]
    tmp += "]\n"
    fw.write(tmp)
            


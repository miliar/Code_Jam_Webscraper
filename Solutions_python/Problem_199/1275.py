import sys
import math

def conversion10(str_list, start, k_pen, str_length):
    if start + k_pen - 1 < str_length:
        for j in range(k_pen):
            if str_list[start+j] == '0':
                str_list[start+j] = '1'
            elif str_list[start+j] == '1':
                str_list[start+j] = '0'
        return str_list;
    else:
        print("error")


testnum = int(input().strip())

for cnum in range(testnum):
    s, k = input().strip().split(' ')
    s = s.replace('+','1')
    s = s.replace('-','0')
    str_len = len(s)
    k = int(k)
    s2 = list(s)

    # conversion to all 1
    cnt_1 = 0   #count the number of conversion
    fail_1 = 0    #record the result of conversion

    for i in range(str_len - k + 1):
        if s2[i] == '0':
            s2 = conversion10(s2,i,k, str_len)
            cnt_1 += 1
    
    for k in range(str_len - k + 1, str_len, 1):
        if s2[k] == '0':
            fail_1 = 1
            break

    if fail_1 == 1:
        print("Case #"+str(cnum+1)+": IMPOSSIBLE")
    elif fail_1 == 0:
        print("Case #"+str(cnum+1)+": "+str(cnt_1))

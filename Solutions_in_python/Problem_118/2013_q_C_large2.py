'''
CodeJam Practice 
Created on 2013-04-13

@author: festony
'''

from cj_lib import *
from properties import *
import math
import time

curr_file_name = 'C-large-2'
#curr_file_name = 'C-large-1'
#curr_file_name = 'C-small-test'
#curr_file_name = 'test'
'''
fair square between [1, 100000000]
'''
arr = [1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002, 10000001, 10011001, 10100101, 10111101, 11000011, 11011011, 11100111, 11111111, 20000002]
arr_str = map(str, arr)
#print arr_str

def calc_1(s):
    x = map(int, s)
    return sum(x)

def gen_pali(half, digit_len):
    if isinstance(half, list):
        half = ''.join(map(str, half))
    if isinstance(half, int):
        half = str(half)
    if digit_len == len(half) * 2:
        return half+''.join(reversed(list(half)))
    else:
        return half+''.join(reversed(list(half)[:-1]))
    
def iter_012(l):
    p = len(l)-1
    l[p] += 1
    carry = l[p] / 3
    l[p] %= 3
    p -= 1
    while p >= 0 and carry > 0:
        l[p] += carry
        carry = l[p] / 3
        l[p] %= 3
        p -= 1
    while carry > 0:
        l.insert(0, carry % 3)
        carry = carry / 3
        
def iter_01(l):
    p = len(l)-1
    l[p] += 1
    carry = l[p] / 2
    l[p] %= 2
    p -= 1
    while p >= 0 and carry > 0:
        l[p] += carry
        carry = l[p] / 2
        l[p] %= 2
        p -= 1
    while carry > 0:
        l.insert(0, carry % 2)
        carry = carry / 2
        

def gen_seq_012(digit_len):
    half_len = int(math.ceil(digit_len / 2.0))
    n = [0]*half_len
    n[0] = 1
    #r = [n[:]]
    r = []
    while len(n) == half_len:
        r.append(gen_pali(n, digit_len))
        iter_012(n)
    return r

def gen_seq_01(digit_len):
    half_len = int(math.ceil(digit_len / 2.0))
    n = [0]*half_len
    n[0] = 1
    #r = [n[:]]
    r = []
    while len(n) == half_len:
        r.append(gen_pali(n, digit_len))
        iter_01(n)
    return r

def gen_seq_01_limit(digit_len):
    half_len = int(math.ceil(digit_len / 2.0))
    n = [0]*half_len
    n[0] = 1
    #r = [n[:]]
    r = []
    while len(n) == half_len:
        t = gen_pali(n, digit_len)
        if calc_1(t) <= 9:
            r.append(t)
        iter_01(n)
    return r

def shift_1(l):
    if l[1] == 1:
        return False
    if sum(l) > 1:
        l.append(0)
    else:
        l.append(1)
    l.pop(0)
    l[0] = 1
    return True

'''
only work with digit_len > 7
generate results like 1xxxxx2xxxxx1
'''
def gen_f_s_with_trailing_2(digit_len):
    half_len = int(math.ceil(digit_len / 2.0))
    if half_len * 2 == digit_len:
        return []
    n = [0]*(half_len-1)
    n[0] = 1
    r = []
    while len(n) == half_len - 1:
        x = n + [2]
        t = gen_pali(x, digit_len)
        #if is_pali(list_sqr(t)):
        r.append(t)
        if not shift_1(n):
            break
    return r

def gen_f_s_with_heading_2(digit_len):
    half_len = int(math.ceil(digit_len / 2.0))
    r = []
    n = [0] * half_len
    n[0] = 2
    t = gen_pali(n, digit_len)
    #if is_pali(list_sqr(t)):
    r.append(t)
    if half_len * 2 == digit_len:
        return r
    n[half_len - 1] = 1
    t = gen_pali(n, digit_len)
    #if is_pali(list_sqr(t)):
    r.append(t)
    return r

def is_pali(x):
    if isinstance(x, list):
        x_str = ''.join(map(str, x))
    else:
        x_str = str(x)
    r_x_str = x_str[::-1]
    return x_str == r_x_str


def find_range(arr, r):
    start = -1
    end = len(arr)
    for i, x in enumerate(arr):
        if x < r[0]:
            start = i
        if x > r[1]:
            end = i
            break
    return end - start - 1


def list_x_digit(l, d):
    r = l[:]
    for i in reversed(range(len(l))):
        r[i] *= d
    carry = 0
    for i in reversed(range(len(l))):
        r[i] += carry
        carry = r[i] / 10
        r[i] %= 10
    while carry > 0:
        r.insert(0, carry % 10)
        carry /= 10
    return r

def list_plus_list(l1, l2):
    if len(l1) < len(l2):
        l1, l2 = l2, l1
    r = l1[:]
    pr = len(r) - 1
    p2 = len(l2) - 1
    while p2 >= 0:
        r[pr] += l2[p2]
        pr -= 1
        p2 -= 1
        
    carry = 0
    for i in reversed(range(len(r))):
        r[i] += carry
        carry = r[i] / 10
        r[i] %= 10
    while carry > 0:
        r.insert(0, carry % 10)
        carry /= 10
    return r
    
        

def list_x_list(l1, l2):
    if len(l1) < len(l2):
        l1, l2 = l2, l1
    #print l1, l2
    r = []
    trail_0 = len(l2) - 1
    for d in l2:
        sub_r = list_x_digit(l1, d)
        sub_r += [0]*trail_0
        trail_0 -= 1
        r = list_plus_list(r, sub_r)
        
    return r

def list_sqr(l):
    if isinstance(l, basestring):
        l = map(int, l)
    l2 = l[:]
    r = list_x_list(l, l2)
    return ''.join(map(str, r))
        

#def input_dividing_func(input_lines):
#    total_case = int(input_lines.pop(0))
#    case_inputs = []
#    for i in range(total_case):
#        case_inputs.append(map(int, input_lines.pop(0).split(' ')))
#    return case_inputs
#def process_func(func_input):
#    #A, B = func_input
#    return 0


#a = [3, 4, 9, 7]
#b = [3, 6, 8]
#print list_x_digit([3, 4, 7, 9], 9)
#print list_x_list(a, b)
#print b, a
#print list_x_list(b, a)
#print b, a
#
#print list_x_list([8, 8, 8], [9, 9, 9])
#print list_sqr([9, 4, 7, 8])

#print list_sqr('4378927')
#print gen_pali('1231', 8)
#print gen_pali('1231', 7)
#print gen_pali([1,2,3,4], 8)
#print gen_pali([1,2,3,4], 7)
#print gen_pali(1654, 8)
#print gen_pali(1654, 7)

#x = gen_seq_012(7)

#print len(x)
#for n in x:
#    print n


#print is_pali('888')
#run_proc(process_func, input_dividing_func, curr_working_folder, curr_file_name)




#################



#for i in range(9, 18):
#    x = gen_seq_012(i)
#    for n in x:
#        if is_pali(list_sqr(n)):
#            arr_str.append(n)
#    print i, 'done'
#print len(arr_str)
#print arr_str

######################

#should be 6

#print gen_f_s_with_trailing_2(13)

#tttt = list_sqr('1100002000011')
#print tttt
#print is_pali(tttt)


#print gen_f_s_with_heading_2(13)

#x = gen_seq_01(12)
#print len(x)
#c = 0
#for n in x:
#    if is_pali(list_sqr(n)):
#        arr_str.append(n)
#        #if calc_1(n) > 9:
#            #print '--------------------------------'
#        c += 1
#    else:
#        print n, list_sqr(n)
#        #if calc_1(n) <= 9:
#        print '--------------------------------'
#print c

#print '%%%%%%%%%%%%%%%%%%'
#x = gen_seq_01_limit(7)
#print len(x)
#c = 0
#for n in x:
#    if is_pali(list_sqr(n)):
#        arr_str.append(n)
#        print n
#        #if calc_1(n) > 9:
#            #print '--------------------------------'
#        c += 1
#    else:
#        #print n, list_sqr(n)
#        #if calc_1(n) <= 9:
#        print '--------------------------------'
##print c
#print '#################################'

def compx(l1, l2):
    if len(l1) > len(l2):
        return 1
    if len(l1) < len(l2):
        return -1
    for i in range(len(l1)):
        if l1[i] > l2[i]:
            return 1
        if l1[i] < l2[i]:
            return -1
    return 0
        
def gen_sqr_pali_max(digit_len):
    half_len = int(math.ceil(digit_len / 2.0))
    max_1 = 4
    is_odd = False
    if digit_len % 2 == 1:
        is_odd = True
    if half_len > max_1:
        max_half = [1] * max_1 + [0] * (half_len - max_1)
    else:
        max_half = [1] * half_len
    if is_odd:
        max_half[half_len - 1] = 1
    return gen_pali(max_half, digit_len)

def gen_sqr_pali_min(digit_len):
    half_len = int(math.ceil(digit_len / 2.0))
    min_half = [1] + [0] * (half_len - 1)
    return gen_pali(min_half, digit_len)

def gen_sqr_pali_lower_upper(l):
    if isinstance(l, basestring):
        l = map(int, l)
    
    l_len = len(l)
    half_len = int(math.ceil(l_len / 2.0))
    prev_half = l[:half_len]
    latt_half = l[-half_len:]
    
    max_1 = 4
    is_odd = False
    if l_len % 2 == 1:
        is_odd = True
    if half_len > max_1:
        max_half = [1] * max_1 + [0] * (half_len - max_1)
    else:
        max_half = [1] * half_len
    if is_odd:
        max_half[half_len - 1] = 1
    min_half = [1] + [0] * (half_len - 1)
        
    shaved_prev_half = [1] * half_len
    for i in range(half_len):
        if prev_half[i] == 0:
            shaved_prev_half[i] = 0
    
    if calc_1(shaved_prev_half) > max_1:
        trim_0 = calc_1(shaved_prev_half) - max_1
        i = half_len - 1
        removed_0 = 0
        while i > 0 and removed_0 < trim_0:
            if shaved_prev_half[i] == 1:
                shaved_prev_half[i] = 0
                removed_0 += 1
            i -= 1
        if removed_0 > 0 and is_odd and shaved_prev_half[half_len - 1] == 0:
            shaved_prev_half[half_len - 1] = 1
    
    shaved_latt_half = shaved_prev_half[::-1]
    lower_bound = []
    if compx(shaved_latt_half, latt_half) > 0:
        if compx(shaved_prev_half, min_half) == 0:
            lower_bound = gen_sqr_pali_max(l_len - 1)
        else:
            lower_bound = gen_pali(shaved_prev_half, l_len)
    else:
        lower_bound = gen_pali(shaved_prev_half, l_len)
    #print 'lower:', lower_bound
    upper_bound = []
    if compx(shaved_prev_half, prev_half) > 0 or (compx(shaved_prev_half, prev_half) == 0 and compx(shaved_latt_half, latt_half) >= 0):
        upper_bound = gen_pali(shaved_prev_half, l_len)
    else:
        if compx(shaved_prev_half, max_half) >= 0:
            upper_bound = gen_sqr_pali_min(l_len + 1)
        else:
            # +1 to prev part and still ensure its sqr pali.
            if calc_1(shaved_prev_half) == max_1:
                i = half_len - 1
                while i >= 0:
                    if shaved_prev_half[i] == 1:
                        shaved_prev_half[i] = 0
                        break
                    i -= 1
                i -= 1
                while i >= 0:
                    if shaved_prev_half[i] == 0:
                        shaved_prev_half[i] = 1
                        break
            else:
                i = half_len - 1
                while i >= 0:
                    if shaved_prev_half[i] == 0:
                        shaved_prev_half[i] = 1
                        break
                    i -= 1
            upper_bound = gen_pali(shaved_prev_half, l_len)
    #print 'upper:', upper_bound
    return [[lower_bound, upper_bound], [gen_pali(min_half, l_len), gen_pali(max_half, l_len)]]




#print gen_sqr_pali_lower_upper('112567842065')      
#print gen_sqr_pali_lower_upper('100000000000')      
#print gen_sqr_pali_lower_upper('110010100111')      

    



#x = gen_seq_01_limit(8)
#print len(x)
#x = gen_seq_01_limit(10)
#print len(x)
#x = gen_seq_01_limit(12)
#print len(x)
#x = gen_seq_01_limit(14)
#print len(x)
#x = gen_seq_01_limit(16)
#print len(x)
#x = gen_seq_01_limit(18)
#print len(x)
#
#print '#################'
#
#def yanghui_tri(h):
#    r = [1]
#    if h == 0:
#        return r
#    r.append(1)
#    if h == 1:
#        return r
#    for i in range(2, h+1):
#        r1 = [r[0]]
#        for j in range(1, i):
#            r1.append(r[j] + r[j-1])
#        r1.append(1)
#        r = r1
#    return r
#x = yanghui_tri(0)
#print sum(x)
#x = yanghui_tri(1)
#print sum(x)
#x = yanghui_tri(2)
#print sum(x)
#x = yanghui_tri(3)
#print sum(x)
#x = yanghui_tri(4)
#print sum(x)
#x = yanghui_tri(5)
#print sum(x)
#x = yanghui_tri(6)
#print sum(x)
#x = yanghui_tri(7)
#print sum(x)
#x = yanghui_tri(8)
#print sum(x)

def add_1_to_half(base_half, r):
    i = len(base_half) - 1
    while i >= 0:
        half = base_half[:]
        if base_half[i] == 1:
            break
        half[i] = 1
        r.append([1] + half[:])
        if sum(half) < min(3, len(half)):
            add_1_to_half(half, r)
        i -= 1

def gen_all_half(half_len):
    r = []
    base_half = [0] * (half_len - 1)
    r.append([1] + base_half[:])
    add_1_to_half(base_half, r)
    
    return r

def gen_all_01(digit_len):
    half_len = digit_len / 2
    is_odd = False
    if digit_len % 2 == 1:
        is_odd = True
    all_half = gen_all_half(half_len)
    r = set([])
    for half in all_half:
        if is_odd:
            r.add(gen_pali(half + [0], digit_len))
            r.add(gen_pali(half + [1], digit_len))
        else:
            r.add(gen_pali(half, digit_len))
    return r

def comp_str_num(s1, s2):
    if len(s1) > len(s2):
        return 1
    if len(s1) < len(s2):
        return -1
    for i in range(len(s1)):
        if s1[i] > s2[i]:
            return 1
        if s1[i] < s2[i]:
            return -1
    return 0

start_time_overall = time.clock()


for i in range(9, 52):
    arr_str += list(gen_all_01(i))
    arr_str += gen_f_s_with_trailing_2(i)
    arr_str += gen_f_s_with_heading_2(i)

arr_str.sort(cmp=comp_str_num)
arr_sqr_str = [0]*len(arr_str)


print len(arr_str)
for i, a in enumerate(arr_str):
    arr_sqr_str[i] = list_sqr(a)
    #print arr_sqr_str[i]

print '--------------------------'

end_time_overall = time.clock()

print("Overall process time: %g sec(s)" % \
(end_time_overall - start_time_overall,))

def find_range_str(arr, r):
    low = r[0]
    up = r[1]
    p = 0
    start = -1
    end = 0
    while p < len(arr):
        if comp_str_num(arr[p], low) < 0:
            start = p
        if comp_str_num(arr[p], up) > 0:
            end = p
            break
        p += 1
#    if start < 0:
#        return 0
#    if end < 0:
#        end = p
    return end-start-1

#print find_range_str(arr_sqr_str, ['1', '104'])

def input_dividing_func(input_lines):
    total_case = int(input_lines.pop(0))
    case_inputs = []
    for i in range(total_case):
        case_inputs.append(input_lines.pop(0).split(' '))
    return case_inputs

def process_func(func_input):
    A, B = func_input
    return find_range_str(arr_sqr_str, [A, B])

run_proc(process_func, input_dividing_func, curr_working_folder, curr_file_name)

#print list_sqr('3213213')

#print len(x)
#for n in sorted(list(x)):
#    print n





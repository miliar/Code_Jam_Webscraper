# Fair and Square - Large 1
# Anish Patel

##FILE_NAME = 'C-sample'
##FILE_NAME = 'C-small-attempt0'
FILE_NAME = 'C-large-1'
##FILE_NAME = 'C-small-practice'

##SIZE = 10**14
##fas_nums = [0] * 39
##
##def is_fair(num):
##    num_str = str(num)
##    num_str_halflen = len(num_str) // 2
##    i = 0
##    while i <= num_str_halflen:
##        if num_str[i] != num_str[-i-1]:
##            return False
##        i += 1
##    return True
####    return num_str == num_str[::-1]
##
##def init_fas_nums():
##    num = 1
##    sq_inc = 3
##    root = 1
##    i = 0
##    while num <= SIZE:
##        if is_fair(num) and is_fair(root):
##            fas_nums[i] = num
##            i += 1
##        num += sq_inc
##        sq_inc += 2
##        root += 1
##init_fas_nums()
##print(fas_nums)
fas_nums = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

from bisect import bisect_left, bisect_right

def find_le_ind(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i-1
    raise ValueError

def find_ge_ind(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return i
    raise ValueError

def do_case():
    begin_num, end_num = get_ints()
    
    begin_ind = find_ge_ind(fas_nums, begin_num)
    end_ind = find_le_ind(fas_nums, end_num)
    n_fas_nums = end_ind - begin_ind + 1
            
    return n_fas_nums    
    
with open('{}.in'.format(FILE_NAME), 'r') as fin:
    with open('{}_large1.out'.format(FILE_NAME), 'w') as fout:
        get_line = lambda: fin.readline()[:-1]
        get_split = lambda: get_line().split()
        get_ints = lambda: (int(i) for i in get_split())
        get_iter = lambda: (item for item in get_split())
        case_out = lambda result: fout.write('Case #{}: {}\n'.format(case, result))
        num_cases = next(get_ints())
        for case in range(1, num_cases+1):
            result = do_case()
            case_out(result)

if __name__ == '__main__':
    print('Completed {}_large1.'.format(FILE_NAME))

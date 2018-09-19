'''
Created on 2013. 4. 13.

@author: purepleya
'''
import math
fair_list = []

def solve():
    make_fair_list()
    global fair_list
    
    f = open('C-large-1.in', 'r') 
    out_file = open('C-large-1.out', 'w')
    
    lines = f.readlines()
    case_count = int(lines[0])
    
    line_no = 0
    for case_n in range(0, case_count):
        line_no += 1
        smallInt = int(lines[line_no].replace('\n', '').split(' ')[0])
        bigInt = int(lines[line_no].replace('\n', '').split(' ')[1])
        
        cnt = 0
        for fair in fair_list:
            if smallInt <= fair and fair <= bigInt:
                 cnt += 1
        
        out_file.write('Case #%d: %d\n' % (case_n + 1, cnt))
    f.close()
    out_file.close()

    


def make_fair_list():
    global fair_list
    
    for i in range(1, 10000000):
        skip_flag = False
        
        for ch_index in (0, str(i).__len__()/2):
            if int(str(i)[ch_index]) < int(str(i)[str(i).__len__() - ch_index - 1]):
                skip_flag = True
                break
        if skip_flag: continue
        
        if is_fair(i):
            if is_fair(i**2):
                fair_list.append(i**2)
#                print '%d - %d' % (i, i**2)

    
def is_fair(input):
    str_input = str(input)
    
    for i in range(0, str_input.__len__() / 2):
        if str_input[i] != str_input[str_input.__len__() - i - 1]:
            return False
    
    return True
    
    
if __name__ == '__main__':
    solve()
'''
Created on 2013. 4. 13.

@author: purepleya
'''
vowels = ('a', 'e', 'i', 'o', 'u')

def solve():
    f = open('A-small-attempt0.in', 'r') 
    out_file = open('A-small-attempt0.out', 'w')
     
    lines = f.readlines()
    line_index = 0
    case_count = int(lines[0])
     
    for case_index in range(0, case_count):
         
        line_index += 1
        L = str(lines[line_index].replace('\n', '').split(' ')[0])
        n = int(lines[line_index].replace('\n', '').split(' ')[1])
         
        core = get_core(L, n)
        reslt = count_case(L, core)
         
        out_file.write('Case #%d: %d\n' % (case_index + 1, reslt.__len__())) 
         
    f.close()
    out_file.close()
    
    print 'finish'
    

def count_case(L, core):
    cases = dict()
    
    for indexs in core:
        for i in range(0, indexs[0] + 1):
            for j in range(indexs[1], len(L)):
                cases[(i, j)] = True
    
    return cases
        
    
    

def get_core(L, n):
    core = []
    for i in range(0, len(L) - n + 1):
        insert_flag = True
        sub_str = L[i: i + n]
        for c in sub_str:
            if insert_flag:
                for v in vowels:
                    if c == v:
                        insert_flag = False
                        break
        if insert_flag:
            core.append([i, i + n - 1])
                 
    return core


if __name__ == '__main__':
    solve()
import sys
case_number = 1
quat = {
    '1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'}, 
    'i':{'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
    'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
    'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'},
    '-1': {'1': '-1', 'i': '-i', 'j': '-j', 'k': '-k'}, 
    '-i':{'1': '-i', 'i': '1', 'j': '-k', 'k': 'j'},
    '-j': {'1': '-j', 'i': 'k', 'j': '1', 'k': '-i'},
    '-k': {'1': '-k', 'i': '-j', 'j': 'i', 'k': '1'}
    }

def look_for_i(string):
    par = quat[string[0]][string[1]]
    for i in range(1, len(string) - 1):
        if (par == 'i'):
            return string[i + 1:len(string)]  
        par = quat[par][string[i + 1]]
    return 0
    
def look_for_j(string):
    par = quat[string[0]][string[1]]
    for i in range(1, len(string) - 1):
        if (par == 'j'):
            return string[i + 1:len(string)]  
        par = quat[par][string[i + 1]]
    return 0
    
def look_for_k(string):
    par = quat[string[0]][string[1]]
    for i in range(1, len(string) - 1):
        par = quat[par][string[i + 1]]
    if(par == 'k'):
        return ''
    else:
        return 0
    


fp =  open(sys.argv[1], 'r')
for i in range(0, int(fp.readline())):
    print('Case #{0}: '.format(case_number), end='')  
    (n_let, rip_let) = fp.readline().strip('\n').split(' ')
    let = fp.readline().strip('\n')
    let = let[0:int(n_let)]
    if (int(n_let) == 1):
        print('NO')
        case_number = case_number + 1
        continue
    
    string = let * int(rip_let)
    
    if (len(string) < 3):
        print('NO')
        case_number = case_number + 1
        continue
        
    if (len(string) == 3):
        print('YES') if string == "ijk" else print('NO')
        case_number = case_number + 1 
        continue
        
    l_f_i = look_for_i(string)
    if (l_f_i != 0 and len(l_f_i) >= 2):
        l_f_j = look_for_j(l_f_i)
        if (l_f_j != 0 and len(l_f_j) >= 2):
            l_f_k = look_for_k(l_f_j)
            if (l_f_k != 0):
                print('YES')
            else:
                print('NO')
        else:
            if (l_f_j == 'k'):
                print('YES')                
            else:
                print('NO')
    else:
        print('NO')
        
    case_number = case_number + 1
fp.close()










"""

"""

import psyco; psyco.full()
#import pyximport; pyximport.install()

def is_eq(P, I, J, L):
    px = 0
    py = 0
    cx = 2 * I + L - 1
    cy = 2 * J + L - 1
    for i in range(I, I+L):
        for j in range(J, J+L):
            if (i, j) not in ((I, J), (I, J+L-1), (I+L-1, J), (I+L-1, J+L-1)):
                px += (2*i - cx) * P[i][j]
                py += (2*j - cy) * P[i][j]
    return 0 == px == py
    

dynamic = True
def solve(case, case_nb=None):
    R, C, D = case[0]
    P = [map(int, line) for line in case[1:]]
    
    
    M = 0
    for I in range(R):
        for J in range(C):
            for L in range(max(3, M+1), min(R-I, C-J)+1):
                if is_eq(P, I, J, L):
                    M = L
    if M >= 3:
        return M
    else:
        return 'IMPOSSIBLE'

def parse_input(dynamic=False):
    from sys import argv, stdin
    def try_int(s):
        try:
            return int(s)
        except:
            return s
    if len(argv) > 1:
        f = open(argv[1])
    else:
        f = stdin
    lines = f.read().split('\n')[0:-1]
    nb_inputs = int(lines[0])
    lines = lines[1:]
    # Number of lines per case
    if not dynamic:
        p = len(lines) / nb_inputs
    line_nb = 0
    for i in range(nb_inputs):
        if dynamic:
            line = map(try_int, lines[line_nb].split(' '))
            p = line[0]
            if len(line) > 1:
                p += 1
            else:
                # I do not take a line that contain only the number of lines
                line_nb += 1
        case_lines = lines[line_nb:line_nb+p]
        case = [map(try_int, line.split(' ')) for line in case_lines[:1]] + case_lines[1:]
        if not dynamic and p == 1:
            case = case[0]
        line_nb += p
        yield case

if __name__ == '__main__':
    for i, case in enumerate(parse_input(dynamic=dynamic)):
        case_nb = 'Case #%i: ' % (i+1)
        result = solve(case, i+1)
        if type(result) is list:
            result = ' '.join(map(str, result))
        elif type(result) is float:
            result = '%.06f' % result
        else:
            result = str(result)
        print case_nb + result

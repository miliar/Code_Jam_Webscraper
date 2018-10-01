import os
import copy

INFILE = r'C:\Users\noam\workspace\CodeJam\input.txt'

def parse_lines(line):
    return list(x for x in line.strip().split() if x)

def solve(input):
    matrix = input
    empty_cells = False
    for i, line in enumerate(matrix):
        if '.' in line:
            empty_cells = True
        matrix[i] = line.strip()
    
    won = {'X': False, 'O': False}
    
    for to_replace in ['X', 'O']:
        cur_mat = copy.deepcopy(matrix)
        
        for i, line in enumerate(cur_mat):
            cur_mat[i] = line.replace('T', to_replace)
        
        expected = ''.join(to_replace*4)
        for i in xrange(4):
            if cur_mat[i] == expected:
                won[to_replace] = True
        
        for i in xrange(4):
            col = ''.join([cur_mat[j][i] for j in xrange(4)])
            if col == expected:
                won[to_replace] = True
                
        if ''.join(cur_mat[i][i] for i in xrange(4)) == expected:
            won[to_replace] = True
        
        if ''.join(cur_mat[3-i][i] for i in xrange(4)) == expected:
            won[to_replace] = True
        
        if won['X']:
            return 'X won'
        
        if won['O']:
            return 'O won'
    
    if empty_cells:
        return 'Game has not completed'
    
    return 'Draw'

def res_to_str(res):
    return str(res)

def main():
    infile = file(INFILE)
    outfile = file(INFILE + '.result.txt', 'wt')
    test_case = 0
    num_str = infile.readline()
    num = int(num_str)
    for case in xrange(num):
        lines = []
        for mat_line in xrange(4):
            lines.append(infile.readline())
        infile.readline()
            
        res = solve(lines)
        str_res = res_to_str(res)
        res_line = 'Case #%d: %s\n' % (case+1, str_res)
        print res_line,
        outfile.write(res_line)
    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()


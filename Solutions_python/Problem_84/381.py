import copy

def solve(input):
    IMP = "Impossible\n"

    input_cp = copy.deepcopy(input)
    for r, line in enumerate(input):
        for c, ch in enumerate(line):
            if ch=='#':
                if c+1==len(line) or r+1==len(input):
                    return IMP
                #print 'BLUE!!!'
                if not (line[c+1] == input[r+1][c] == input[r+1][c+1] == '#'):
                    return IMP
                line[c] = '/'
                line[c+1] = '\\'
                input[r+1][c] = '\\'
                input[r+1][c+1] = '/'
                
    #print input
    ans = ""
    for line in input:    
        ans += "".join(line) 

    return ans 

if __name__ == '__main__':
    #str_in = 'A-small-attempt0.in'
    str_in = 'A-large.in'
    #str_in = 'A-test.in'
    f_out = open(str_in.rstrip('.in') + '.out', 'w')
    f_in = open(str_in)
    N = int(f_in.next())
    
    
    for num_q in range(N):
        R, C = [int(_) for _ in f_in.next().split()]
        question = [list(f_in.next()) for _ in range(R)]
        output = 'Case #' + str(num_q + 1) + ': ' + '\n' + solve(question) 
        f_out.write(output); print output,

    f_in.close()
    f_out.close()
    
    #print 'exit'
    #print A_D, set_A


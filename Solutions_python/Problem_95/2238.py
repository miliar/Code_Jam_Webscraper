import copy

def solve(input):
    before = 'abcdefghijklmnopqrstuvwxyz '
    after = 'yhesocvxduiglbkrztnwjpfmaq '
    ans = ""
    
    for c in input:
        ans += after[before.find(c)]
    return ans

if __name__ == '__main__':
    str_in = 'A-small-attempt0.in'
    #str_in = 'A-large.in'
    #str_in = 'A-test.in'
    f_out = open(str_in.rstrip('.in') + '.out', 'w')
    f_in = open(str_in)
    N = int(f_in.next())
    
    
    for num_q in range(N):
        question = f_in.next()
        output = 'Case #' + str(num_q + 1) + ': ' + solve(question) +'\n'
        f_out.write(output); print output,

    f_in.close()
    f_out.close()
    
    #print 'exit'
    #print A_D, set_A


inputfile = r'A-large.in'
outputfile = r'A-large.out'

#input
def input_data():
    import os
    os.chdir(r'C:\codejam')
    FILENAME = inputfile 
    f = open(FILENAME)
    lines = f.readlines()
    f.close()
    return lines

#output
def output_data(ans):    
    fout = open(outputfile, 'wt')
    print(ans, file = fout)
    fout.close()




if __name__ == '__main__':
    lines = input_data()

    #calc
    T = int(lines.pop(0)[:-1])
    ans = ''
    for i_t in range(T):
        D, N = map(int, lines.pop(0)[:-1].split())
        max_t = 0
        for i_n in range(N):
            K, S = map(int, lines.pop(0)[:-1].split())
            t = (D - K) / float(S)
            max_t = max(max_t, t)
        sa = D / max_t
        ansline = 'Case #' + str(i_t+1) + ': %.7f' % round(sa, 7) + '\n'
        ans += ansline
##        for e in list_ans:
##            ans += e + '\n'
    output_data(ans)

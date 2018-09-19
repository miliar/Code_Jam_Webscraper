

def output_matrix(M):
    for row in M:
        print row

def check_who_win(array):
    winner_mapping = {4:'X won', 3:'X won', -4:'O won', -3:'O won'}
    sum_of_array = sum(array)
    if winner_mapping.has_key(sum_of_array):
        return winner_mapping[sum_of_array]
    else:
        return None



def check_status_of_matrix(M, flag_full):

    for i in range(4):
        # check row
        winner = check_who_win(M[i][:])
        if winner:
            return winner

        # check column
        winner = check_who_win([M[j][i] for j in range(4)])
        if winner:
            return winner
    #check diagonal
    winner = check_who_win([M[i][i] for i in range(4)])
    if winner:
        return winner
    #check anti-diagonal
    winner = check_who_win([M[i][3-i] for i in range(4)])
    if winner:
        return winner

    if flag_full:
        return 'Draw'
    else:
        return 'Game has not completed'



if __name__ == '__main__':
    fin_path = './input/A-large.in'
    fout_path = './input/A-large.out'
    fin = open(fin_path)
    fout = open(fout_path, 'w')
    num_of_cases = int(fin.readline())
    for cid in range(num_of_cases):
        Matrix = [[0 for x in range(4)] for x in range(4)]
        flag_full = True
        for i in range(4):
            mapping = {'X':1,'O':-1, '.':100, 'T':0}
            row = fin.readline().split()[0]
            Matrix[i] = [mapping[x] for x in iter(row)]
            if '.' in row:
                flag_full = False

        fin.readline() #read empty line
        print "case ", cid+1
#        output_matrix(Matrix)

        winner=check_status_of_matrix(Matrix, flag_full)
        fout.write('Case #%d: %s\n'%(cid+1,winner))

    fin.close()
    fout.close()


        


  
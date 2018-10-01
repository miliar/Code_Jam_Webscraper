def main():
    f = open('A-small-attempt1.in','r')
    out = open('out.txt','w')
    N = int(f.readline())

    game = 1
    while game < N+1:
        matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        rows = []
        win = 0
        for j in range(0,4):
            rows.append(f.readline())
        f.readline()
        for j in range(0,4):
            for k in range(0,4):
                if rows[j][k] == 'X':
                    matrix[j][k] = 1
                elif rows[j][k] == 'O':
                    matrix[j][k] = -1
                else:
                    matrix[j][k] = 0
            rowsum = matrix[j][0] + matrix[j][1] + matrix[j][2] + matrix[j][3]
            if rowsum == 4 or (rowsum == 3 and 'T' in rows[j]):
                out.write('Case #' + str(game) + ': X won')
                win = 1
                game += 1
                break
            if rowsum == -4 or (rowsum == -3 and 'T' in rows[j]):
                out.write('Case #' + str(game) + ': O won')
                win = 1
                game += 1
                break
        if win != 1:
            for j in range(0,4):
                colsum = matrix[0][j] + matrix[1][j] + matrix[2][j] + matrix[3][j]
                m = [rows[0][j],rows[1][j],rows[2][j],rows[3][j]]
                if colsum == 4 or (colsum == 3 and 'T' in m):
                    out.write('Case #' + str(game) + ': X won')
                    win = 1
                    game += 1
                    break
                if colsum == -4 or (colsum == -3 and 'T' in m):
                    out.write('Case #' + str(game) + ': O won')
                    win = 1
                    game += 1
                    break
        if win != 1:
            diagsum = matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[3][3]
        
            m = [rows[0][0],rows[1][1],rows[2][2],rows[3][3]]
            if diagsum == 4 or (diagsum == 3 and 'T' in m):
                out.write('Case #' + str(game) + ': X won')
                win = 1
                game += 1
                
            if diagsum == -4 or (diagsum == -3 and 'T' in m):
                out.write('Case #' + str(game) + ': O won')
                win = 1
                game += 1
                
        if win != 1:
            diagsum = matrix[0][3] + matrix[1][2] + matrix[2][1] + matrix[3][0]
            m = [rows[3][0],rows[2][1],rows[2][1],rows[3][0]]
            if diagsum == 4 or (diagsum == 3 and 'T' in m):
                out.write('Case #' + str(game) + ': X won')
                win = 1
                game += 1
                
            if diagsum == -4 or (diagsum == -3 and 'T' in m):
                out.write('Case #' + str(game) + ': O won')
                win = 1
                game += 1
        # no winner.
        if win != 1:
            draw = 0
            for i in rows:
                for j in i:
                    if j == '.':
                        draw = 1
                        break
            if draw != 1:
                out.write('Case #' + str(game) + ': Draw')
            else:
                out.write('Case #' + str(game) + ': Game has not completed')
            game += 1
        out.write('\n')
    out.close()
main()

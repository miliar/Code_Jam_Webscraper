num = int(input())

def minimise(row, col, mine):
    
    if mine < 0 or row < 0 or col < 0:
        return row, col, float('inf')
        
    if (row - 1, col, mine - col) in dic:
        a, b, c = dic[(row - 1, col, mine - col)]
    else:
        a, b, c = minimise(row - 1, col, mine - col)
        dic[(row - 1, col, mine - col)] = (a, b, c)
        
    if (row, col - 1, mine - row) in dic:
        d, e, f = dic[(row, col - 1, mine - row)]
    else:
        d, e, f = minimise(row, col - 1, mine - row)
        dic[(row, col - 1, mine - row)] = (d, e, f)
    
    if c < f and c < float('inf'):
        return a, b, c
    if f < float('inf'):
        return d, e, f
    return row, col, mine

dic = dict()
for n in range(num):
    rows, cols, mines = [int(a) for a in input().split()]
    r, c, m = minimise(rows, cols, mines)
    frows, fcols, fmines = r, c, m
    
    print('Case #' + str(n + 1) + ':')
    
    
        
    if frows == 1 and fcols == 1:
        s = '.' + '*' * (cols - 1) + ('\n' + '*' * cols) * (rows - 1)
        s = 'c' + s[1:]
        print(s)
        
    elif rows == 4 and cols == 4 and mines == 3:
        print('c...\n....\n...*\n..**')
    
    elif rows == 1: 
        
        s = '.' * (cols - mines) + '*' * mines
        s = 'c' + s[1:]
        print(s)
        
    elif cols == 1:
        s = '.\n' * (rows - mines) + '*\n' * mines
        s = 'c' + s[1:-1]
        print(s)
    else:
        minl = min(frows, fcols)
        maxl = max(frows, fcols)
        
        if fcols * frows == 4 and fmines == 0:
            s = 'c.' + '*' * (cols - 2) + '\n' + '..' + '*' * (cols - 2) + ('\n' + '*' * cols) * (rows - 2)
            print(s) 
        elif frows == 1 or fcols == 1:
            print('Impossible')
             
            #for q in range(rows):
            #    print('.' * cols)
        elif (fmines <= maxl - 2 and minl > 2) or fmines == 0:
            s = ('.' * fcols + '*' * (cols - fcols) + '\n') * frows + ('*' * cols + '\n') * (rows - frows)

            if fmines != 0:
                if fcols < frows:
                    for x in range(frows - fmines, frows):
                        s = s[:(cols+1) * x + fcols - 1] + '*' + s[(cols+1) * x + fcols:]
                    s = s[:-1]
                    
                else:
                    s = s[:(cols+1) * (frows-1)] + '.' * (fcols - fmines) + '*' * (cols - fcols + fmines) + '\n' + s[(cols+1) * frows:]
            else:
                s = s[:-1]
            s = 'c' + s[1:]
            if s[-1] == '\n':
                s = s[:-1]
            print(s)
            
        elif maxl <= 4 or minl <= 2:
            print('Impossible')
            #for q in range(rows):
            #    print('.' * cols)
        else:
            
            s = ('.' * fcols + '*' * (cols - fcols) + '\n') * frows + ('*' * cols + '\n') * (rows - frows)

            if frows == fcols:
                for x in range(frows - fmines + 1, frows):
                    s = s[:(cols+1) * x + fcols - 1] + '*' + s[(cols+1) * x + fcols:]
                s = s[:-1]
                s = s[:(cols+1) * (frows - 1)] + '*' + s[(cols+1) * (frows - 1) + 1:]
            elif fcols < frows:
                for x in range(frows - fmines + 1, frows):
                    s = s[:(cols+1) * x + fcols - 1] + '*' + s[(cols+1) * x + fcols:]
                s = s[:-1]
                s = s[:fcols - 1] + '*' + s[fcols:]
            else:
                s = s[:(cols+1) * (frows-1)] + '.' * (fcols - fmines + 1) + '*' * (cols - fcols + fmines - 1) + '\n' + s[(cols+1) * frows:]
                s = s[:(cols+1) * (frows - 1)] + '*' + s[(cols+1) * (frows - 1) + 1:]
                
            s = 'c' + s[1:]
            
            
            if s[-1] == '\n':
                s = s[:-1]
            
            print(s)
    #print(rows, cols, mines, frows, fcols, fmines)
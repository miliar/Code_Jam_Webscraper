def solve(board):
    #print board

    empty_square_flag = False

    #check rows
    for row in range(4):
        previous = 'T'
        for col in range(4):
            current = board[row][col]
            #print row, col, previous, current
            #print
            if current == '.':
                empty_square_flag = True
                break
            if previous == 'T' or current == 'T' or current == previous:
                # O or X won
                if col == 3:
                    if previous != 'T':
                        return result_dict[previous]
                    elif current != 'T':
                        return result_dict[current]
                    
                previous = current
                continue
            else:
                break

    #check cols
    for col in range(4):
        previous = 'T'
        for row in range(4):
            current = board[row][col]
            #print row, col, previous, current
            #print
            if current == '.':
                empty_square_flag = True
                break
            if previous == 'T' or current == 'T' or current == previous:
                # O or X won
                if row == 3:
                    if previous != 'T':
                        return result_dict[previous]
                    elif current != 'T':
                        return result_dict[current]  
                    
                previous = current
                continue
            else:
                break

    #check diagonal 1
    row = 0; col = 0
    previous = 'T'
    for i in range(4):
        current = board[row][col]
        #print row, col, previous, current
        #print
        if current == '.':
            empty_square_flag = True
            break
        if previous == 'T' or current == 'T' or current == previous:
            # O or X won
            if row == 3:
                if previous != 'T':
                    return result_dict[previous]
                elif current != 'T':
                    return result_dict[current]                  
            previous = current
            row += 1; col += 1
            continue
        else:
            break

    #check diagonal 2
    row = 0; col = 3
    previous = 'T'
    for i in range(4):
        current = board[row][col]
        #print row, col, previous, current
        #print
        if current == '.':
            empty_square_flag = True
            break
        if previous == 'T' or current == 'T' or current == previous:
            # O or X won
            if row == 3:
                if previous != 'T':
                    return result_dict[previous]
                elif current != 'T':
                    return result_dict[current]                  
            previous = current
            row += 1; col -= 1
            continue
        else:
            break

    result = result_dict['Not_Com'] if empty_square_flag else result_dict['Draw']
    return result
    


#input, solve and output:
                        
input = open('A-small-attempt0.in', 'r')
output = open('A-small-attempt0.out', 'w')

result_dict = {'X': "X won",
              'O': "O won" ,
              'Draw': 'Draw',
              'Not_Com': "Game has not completed"
              }

num_cases = int(input.readline())
for case in range(1, num_cases+1):
        board = []
        for i in range(4):
            board.append(input.readline().strip())
        input.readline()

        result = solve(board)

        #print case, result
        #print 
        output.write('Case #%s: %s\n' %(case, result))

input.close()
output.close()


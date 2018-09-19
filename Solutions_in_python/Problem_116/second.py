
def won(matrix):
    complete = True
    for i in range(4):
        init_type = matrix[i][0]
        if init_type ==  "T":
            init_type = matrix[i][1]
        won = True
        for j in range(1,4):
            if init_type == ".":
                complete = False
                won = False
                break
            if matrix[i][j] != "T" and matrix[i][j] != init_type:
                if matrix[i][j] == ".":
                    complete= False
                won = False
                break
        if won:
            return init_type
        
    for i in range(4):
        init_type = matrix[0][i]
        if init_type ==  "T":
            init_type = matrix[1][i]
        won = True
        for j in range(1,4):
            if init_type == ".":
                complete = False
                won = False
                break
            if matrix[j][i] != "T" and matrix[j][i] != init_type:
                if matrix[j][i] == ".":
                    complete= False
                won = False
                break
        if won:
            return init_type
    
    init_type = matrix[0][0]
    if init_type ==  "T":
        init_type = matrix[1][1]
    for i in range(1,4):
        won = True
        if init_type == ".":
            complete = False
            won = False
            break
        if matrix[i][i] != "T" and matrix[i][i] != init_type:
            if matrix[j][i] == ".":
                complete= False
            won = False
            break
    if won:
        return init_type
        
    init_type = matrix[0][3]
    if init_type ==  "T":
        init_type = matrix[1][2]
    for i in range(1,4):
        won = True
        if init_type == ".":
            complete = False
            won = False
            break
        if matrix[0+i][3-i] != "T" and matrix[0+i][3-i] != init_type:
            if matrix[j][i] == ".":
                complete= False
            won = False
            break
    if won:
        return init_type
    return complete
    
if __name__ == "__main__":
    with open("A-small-attempt1.in", "r") as f:
        content = f.readlines()
    case_count = content[0]
    for i in range(int(case_count)):
        matrix = []
        for j in range(1,5):
            matrix.append(content[i*5 + j])
        result = won(matrix)
        if result == "X" or result == "O":
            print "Case #%d: %s won" % (i+1, result)
        elif result:
            print "Case #%d: Draw" % (i+1)
        else:
            print "Case #%d: Game has not completed" % (i+1)
            
                
            
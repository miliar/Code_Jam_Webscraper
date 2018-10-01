
import time


input_file = 'C-large.in'
input_file = 'C-small-attempt2.in'
#input_file = 'C0.txt'

output_file = input_file + '.txt'

DEBUG = False
def dummy(*args, **kwargs):
    pass
debug = print if DEBUG else dummy
        
def process_cases(input_file, output_file):
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        nr_cases = int(fin.readline())
        print('--> Test cases: %d' % nr_cases)
        for c in range(nr_cases):
            if c % 100 == 0: 
                print('--> %d' % (c + 1))
            else:
                debug('--> %d' % (c + 1))
            result = solve_case(fin)
            debug('\n')
            debug(result)
            debug('\n')
            fout.write('Case #%d: \n%s\n' % (c + 1, str(result)))

#----------------------------------------------------------------------------------------------------------------------            

def solve_case(file):
    UNK, CLICK, MINE = '.c*'
    CLICK = 'c'
    MINE = '*'
    IMP = 'Impossible'
    rows, cols, mines = list(map(int, file.readline().strip().split()))
    debug('R=%d C=%d M=%d' % (rows, cols, mines))
    area = rows * cols
    
    #joinit = lambda matrix: '\n'.join(''.join(line) for line in matrix)
    
    mines_orig = mines
    def joinit(matrix):
        result = '\n'.join(''.join(line) for line in matrix)
        assert len(result) == rows * cols + rows - 1
        assert result.count(MINE) == mines_orig
        assert result.count(CLICK) == 1
        return result
    
    if mines >= area:
        return IMP
        
    if mines + 1 == area:
        board = [([MINE] * cols) for i in range(rows)]
        board[0][cols - 1] = CLICK
        return joinit(board)
        
    if mines == 0:
        board = [([UNK] * cols) for i in range(rows)]
        board[0][cols - 1] = CLICK
        return joinit(board)
            
    if rows == 1 or cols == 1:
        board = [[MINE] * mines + [UNK] * (area - mines - 1) + [CLICK]]
        if cols == 1:
            board = zip(*board)
        return joinit(board)
        
    if rows == 2 or cols == 2:
        if ((area - mines) % 2 == 1) or ((area - mines) == 2):
            return IMP
        board = [([MINE] * (mines//2) + [UNK] * ((area - mines)//2)) for i in range(2)]
        board[0][area//2 - 1] = CLICK
        if cols == 2:
            board = zip(*board)
        return joinit(board)
        
    # both sides >= 3

    if (area - mines) in [7, 5, 3, 2]:
        return IMP
    
    # fill bottom with mines
    
    mines_bottom = min(mines, (rows - 3) * cols)
    rows_mines = mines_bottom // cols
    rows_clear = rows - 3 - rows_mines
    leftover = mines_bottom % cols
    row_leftover = []
    if leftover > 0:
        row_leftover = [[MINE] * leftover + [UNK] * (cols - leftover)]
        rows_clear -= 1
    board_bottom = [[UNK] * cols] * rows_clear + row_leftover + [[MINE] * cols] * rows_mines
    
    board = [([UNK] * cols) for i in range(3)]
    board[0][cols-1] = CLICK
    board += board_bottom
    
    if leftover == cols - 1:
        board[3 + rows_clear - 1][0] = MINE
        board[3 + rows_clear][cols - 2] = UNK
    
    mines -= mines_bottom
    area = 3 * cols

    if mines <= (cols - 2):
        for c in range(mines):
            board[2][c] = MINE
        return joinit(board)
        
    if mines <= (area - 9):
        if (mines - cols + 2) % 2 == 0:
            for c in range(cols - 2):
                board[2][c] = MINE
            col_mines = (mines - cols + 2) // 2
            for c in range(col_mines):
                board[0][c] = MINE
                board[1][c] = MINE
        else:
            for c in range(cols - 3):
                board[2][c] = MINE
            col_mines = (mines - cols + 3) // 2
            for c in range(col_mines):
                board[0][c] = MINE
                board[1][c] = MINE
        return joinit(board)
        
    for c in range(cols - 3):
        board[0][c] = MINE
        board[1][c] = MINE
        board[2][c] = MINE
    
    if mines >= (area - 8):
        board[2][cols-3] = MINE
    if mines >= (area - 6):
        board[0][cols-3] = MINE
        board[1][cols-3] = MINE
    if mines >= (area - 4):
        board[2][cols-2] = MINE
        board[2][cols-1] = MINE

    return joinit(board)

#----------------------------------------------------------------------------------------------------------------------            
    
if __name__ == "__main__":
    start_time = time.perf_counter()
    process_cases(input_file, output_file)
    print('--> Total time: %.2f' % (time.perf_counter() - start_time))
import sys

def main():
    f = open(sys.argv[1], 'r+')
    num_games = int(f.readline())
    all_lines = f.readlines()

    for num in range(0,num_games):
        lines = all_lines[(num*5):(num*5+4)]
        h = horiz(lines)
        v = vert(lines)
        d = diag(lines)
        if h:
            print 'Case #' + str(num+1) + ': ' + h + ' won'
        
        elif v:
            print 'Case #' + str(num+1) + ': ' + v + ' won'
        
        elif d:
            print 'Case #' + str(num+1) + ': ' + d + ' won'
        
        elif(draw(lines)):
            print 'Case #' + str(num+1) + ': Draw'
        
        else:
            print 'Case #' + str(num+1) + ': Game has not completed'
            
        
def horiz(lines):
    for line in lines:
        line = line.strip()
        for play in ['X', 'O']:
            if line.count(play) == 4:
                return play
            elif line.count(play) == 3:
                if line.count('T') == 1:
                    return play 
            
def vert(lines):
    for i in range(0,4):
        vert_line = [row[i] for row in lines]
        for play in ['X', 'O']:
            if vert_line.count(play) == 4:
                return play
            elif vert_line.count(play) == 3:
                if vert_line.count('T') == 1:
                    return play
def diag(lines):
    diag_lines = []
    f_line = []
    b_line = []
    for i in range(0,4):
        f_line.append(lines[i][i])
        b_line.append(lines[i][-i-2])
    diag_lines.append(f_line)
    diag_lines.append(b_line)
        
    for line in diag_lines:
        for play in ['X', 'O']:
            if line.count(play) == 4:
                return play
            elif line.count(play) == 3:
                if line.count('T') == 1:
                    return play 

def draw(lines):
    for line in lines:
        for char in line[0:4]:
            if char == '.':
                return False
    return True
        
    



    
if __name__ == "__main__":
    main()

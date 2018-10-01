#!/usr/local/Cellar/python3/3.2.2/bin/python3

from GCJ import GCJ

def check(pivot, char):
    if not pivot or pivot == '.':
        return False
    elif pivot == 'T':
        pivot = char
    elif char == 'T':
        return pivot
    elif pivot != char:
        return False
    else:
        return pivot
        

def solve(infile):
    data = [[ch for ch in infile.readline().strip()] for i in range(4)]
    infile.readline()
    draw = True
    print(data)
    win_d1 = data[0][0]
    win_d2 = data[0][3]
    for x in range(4):
        win_h = data[x][0]
        win_v = data[0][x]
        win_d1 = check(win_d1, data[x][x])
        win_d2 = check(win_d2, data[x][3-x]) 
        for y in range(3):
            win_h = check(win_h, data[x][y+1])
            win_v = check(win_v, data[y+1][x])
            if data[y+1][x] == '.':
                draw = False
        if win_h or win_v:
            return (win_h or win_v) + " won"
        
    if win_d1:
        return win_d1 + " won"
    elif win_d2:
        return  win_d2 + " won"
    if draw:
        return "Draw"
    else:
        return "Game has not completed"

if __name__ == "__main__":
    GCJ("A", solve).run()

    

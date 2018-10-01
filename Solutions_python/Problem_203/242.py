import copy
import sys

def solve(R,C,lines):
    solved = True
    
    #fill down
    for r in range(1,R):
        for c in range(C):
            
            if lines[r][c] != "?":
                continue
            
            char = lines[r-1][c]
            
            if char == "?":
                continue
            
            valid = True

            left = c
            while left > 0 and lines[r-1][left-1] == char:
                left -= 1
                if lines[r][left] != "?":
                    valid = False
                    break

            if not valid:
                continue

            right = c
            while right < C-1 and lines[r-1][right+1] == char:
                right += 1
                if lines[r][right] != "?":
                    valid = False
                    break

            if not valid:
                continue

            newlines = copy.deepcopy(lines)
            for i in range(left, right+1):
                newlines[r][i] = char

            soln = solve(R,C,newlines)
            if soln:
                return soln
                
    #fill up
    for r in range(R-1):
        for c in range(C):

            if lines[r][c] != "?":
                continue

            char = lines[r+1][c]
            
            if char == "?":
                continue
                
            valid = True

            left = c
            while left > 0 and lines[r+1][left-1] == char:
                left -= 1
                if lines[r][left] != "?":
                    valid = False
                    break

            if not valid:
                continue

            right = c
            while right < C-1 and lines[r+1][right+1] == char:
                right += 1
                if lines[r][right] != "?":
                    valid = False
                    break

            if not valid:
                continue

            newlines = copy.deepcopy(lines)
            for i in range(left, right+1):
                newlines[r][i] = char

            soln = solve(R,C,newlines)
            if soln:
                return soln
            
    #fill right
    for r in range(R):
        for c in range(1,C):

            if lines[r][c] != "?":
                continue

            char = lines[r][c-1]
            
            if char == "?":
                continue
                
            valid = True

            up = r
            while up > 0 and lines[up-1][c-1] == char:
                up -= 1
                if lines[up][c] != "?":
                    valid = False
                    break

            if not valid:
                continue

            down = r
            while down < R-1 and lines[down+1][c-1] == char:
                down += 1
                if lines[down][c] != "?":
                    valid = False
                    break

            if not valid:
                continue

            newlines = copy.deepcopy(lines)
            for i in range(up, down+1):
                newlines[i][c] = char

            soln = solve(R,C,newlines)
            if soln:
                return soln

    #fill left
    for r in range(R):
        for c in range(0,C-1):

            if lines[r][c] != "?":
                continue

            char = lines[r][c+1]
            
            if char == "?":
                continue
                
            valid = True

            up = r
            while up > 0 and lines[up-1][c+1] == char:
                up -= 1
                if lines[up][c] != "?":
                    valid = False
                    break

            if not valid:
                continue

            down = r
            while down < R-1 and lines[down+1][c+1] == char:
                down += 1
                if lines[down][c] != "?":
                    valid = False
                    break

            if not valid:
                continue

            newlines = copy.deepcopy(lines)
            for i in range(up, down+1):
                newlines[i][c] = char

            soln = solve(R,C,newlines)
            if soln:
                return soln

            
            
    if solved:
        return lines
                    

                    
def parse(text):
    T = int(text.next())
    for i in range(T):
        line = text.next().rstrip().split(" ")
        R = int(line[0])
        C = int(line[1])
        
        lines = []
        for j in range(R):
            line = [x for x in text.next().rstrip()]
            lines.append(line)
            
        soln = solve(R,C,lines)
        
        print "Case #%d:" % (i+1)
        for line in soln:
            print "".join(line)

parse(sys.stdin)
			

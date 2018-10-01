import sys
import os, stat

def main():
    mode = os.fstat(0).st_mode
    input = None
    if stat.S_ISFIFO(mode):
        #print "stdin is piped"
        input = open("input.txt")
    elif stat.S_ISREG(mode):
        #print "stdin is redirected"
        input = sys.stdin
    else:
        #print "stdin is terminal"
        input = open("input.txt")

    numCases = int(input.readline().rstrip('\n'))
    count = 0
    for i in range(numCases):
        firstLine = input.readline().rstrip('\n')
        numRows = int(firstLine.partition(' ')[0])
        numCols = int(firstLine.partition(' ')[2])
        count += 1
        if (count == 0):
            print '\n'
        lines = [input.readline().rstrip('\n') for j in range(numRows)]
        print 'Case #%d:\n%s'%(i+1, '\n'.join(evaluate(lines, numRows, numCols)))
        count += numRows
    # numLines = int(input.readline())
    # lines = [input.readline().rstrip('\n') for i in range(numLines)]
    # for (i,line) in enumerate(lines):
    #     print 'Case #%d: %s'%(i+1, str(evaluate(line)))

def csplit(line, separator):
    for part in line.split(separator):
        try:
            yield int(part)
        except:
            yield str(part)

def evaluate(grid, numRows, numCols):
    found_chars = []
    for i in range(numRows):
        for j in range(numCols):
            if not grid[i][j] in found_chars and grid[i][j] != '?':
                found_char = grid[i][j]
                start = j
                end = j+1
                for k in range(j-1, -1, -1):
                    if grid[i][k] == '?':
                        start -= 1
                    else:
                        break
                for k in range(j+1,numCols):
                    if grid[i][k] == '?':
                        end += 1
                    else:
                        break
                for k in range(i, numRows):
                    if k == i or grid[k][start:end].count('?') == end-start:
                        grid[k] = grid[k][:start] + found_char*(end-start) + grid[k][end:]
                    else:
                        break
                found_chars.insert(0, found_char)
    for i in range(numRows-1, -1, -1):
        if '?' in grid[i]:
            grid[i] = grid[i+1]
    return grid


main()


import os, sys

def solve(infile, case_id):
    lawn = list()
    width, height = [int(item) for item in infile.readline().split()]
    for i in range(width):
        line = [int(item) for item in infile.readline().split()]
        lawn.append(line)
    
    good = parse(lawn, width, height)
    print "Case #%d: %s" % (case_id, "YES" if good else "NO")
    
def parse(lawn, width, height):
    row_max = [max(line) for line in lawn]
    column_max = list()
    for h in range(height):
        cur_max = 0
        for w in range(width):
            cur_max = max(cur_max, lawn[w][h])
        column_max.append(cur_max)

    for i, line in enumerate(lawn):
        for j, h in enumerate(line):
            if h < row_max[i] and h < column_max[j]:
                return False
    
    return True
    

def main(infile):
    case_num = int(infile.readline())
    for i in range(case_num):
        solve(infile, i + 1)

if __name__ == "__main__":
    main(sys.stdin)

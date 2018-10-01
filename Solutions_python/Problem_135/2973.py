import sys

OUTFILE = "ans.out"

def solve(inp):
    outfile = open(OUTFILE,'w')
    lines = [x.rstrip() for x in inp.readlines()]
    lines = [[int(y) for y in x.split()] if len(x) > 1 else int(x) for x in lines] 
    T = lines[0]
    lines = lines[1:]
    case = 1
    for i in xrange(0,len(lines),10):
        choice1 = lines[i]
        grid1   = lines[i+1:i+5]
        choice2 = lines[i+5]
        grid2   = lines[i+6:i+10]
        intersect = intersection(grid1[choice1-1], grid2[choice2-1])
        outfile.write("Case #"+str(case) + ": ")
        if len(intersect) == 1:
            outfile.write(str(intersect.pop())+'\n')
        elif len(intersect) == 0:
            outfile.write("Volunteer cheated!"+'\n')
        else:
            outfile.write("Bad magician!"+'\n')
        case += 1

def intersection(list1, list2):
    return set(list1).intersection(list2)
        

if __name__ == "__main__":
    solve(open(sys.argv[1]))

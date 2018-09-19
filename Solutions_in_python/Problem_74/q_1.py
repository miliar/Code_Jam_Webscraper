## QUESTION 1

def calc(lst):
    loc_orange = 1
    loc_blue = 1
    t_orange = 0
    t_blue = 0
    for i in range(int(lst[0])):
        if lst[2*i + 1] == 'O':
            t_orange = max(t_blue + 1, t_orange + abs(loc_orange - int(lst[2*i + 2])) + 1)
            loc_orange = int(lst[2*i+2])
        if lst[2*i + 1] == 'B':
            t_blue = max(t_orange + 1, t_blue + abs(loc_blue - int(lst[2*i + 2])) + 1)
            loc_blue = int(lst[2*i+2])

    return max(t_orange, t_blue)
            
def solve(filename, out_file):
    lines = [x[:-1] for x in open(filename).readlines()]
    out = open(out_file, 'a')
    times = int(lines[0])
    for i in range(1, times + 1):
        out.writelines('Case #%d: %d\n' % (i, calc(lines[i].split(' '))))

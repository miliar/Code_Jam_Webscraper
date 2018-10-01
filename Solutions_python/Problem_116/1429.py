result_string = ['O won','X won', 'Draw', 'Game has not completed']
win_index = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16], [1, 6, 11, 16], [4, 7, 10, 13]]

def print_result(f, c, r):
    f.write("Case #%d: %s\n" % (c, result_string[r]))

def create_winlist():
    l = []
    l.extend([[i for i in xrange(j,j+4)] for j in xrange(1,16, 4)])
    l.extend([[i for i in xrange(j,17,4)] for j in xrange(1,5)])
    l.append([1,6,11,16])
    return l

def make_board(f):
    od = {}
    xd = {}
    l = ''
    for i in xrange(4):
        ll = f.readline().strip()
        l += ll
    f.readline()
    od = l.replace('T', 'O')
    xd = l.replace('T', 'X')
    return(od, xd)

def check_win(l, p):
    w = [p]*4
    for i in win_index:
        if w == [l[j-1] for j in i]:
            return True
    return False

def main():
    f = open("A-large.in")
    fo = open("A-large.out", 'w')
    size = int(f.readline())
    for i in xrange(1, size+1):
        od, xd = make_board(f)
        if check_win(od, 'O'):
            print_result(fo, i, 0)
        elif check_win(xd, 'X'):
            print_result(fo, i, 1)
        elif '.' in od:
            print_result(fo, i, 3)
        else:
            print_result(fo, i, 2)
    f.close()
    fo.close()
main()

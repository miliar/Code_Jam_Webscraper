__author__ = 'Javi'

#pieces = {1:[(1,1)], 2:[(1,2)],3:[(3,1), (2,2)], 4:[(4,1),(3,2),(2,2),(4,2)] }
pieces = {1:[], 2:[],3:[1], 4:[2,1] }



def main():
    lines = tuple(open('D-small-attempt1.in', 'r'))
    num_inputs = int(lines[0])
    num_lines_read = 0

    f = open('D.out', 'w')

    for i in xrange(num_inputs):
        X,R,C = map(int,lines[1 + i].strip().split(' '))

        gabrielWin = False
        if R*C % X == 0 and X <= max(R,C) and  R not in pieces[X] and C not in pieces[X]:
            gabrielWin = True

            # gabrielWin = True
            # for a,b in pieces[X]:
            #     if max(a,b) > min(R,C) and (R % a == 0 and C % b != 0 or R % b == 0 and C % a != 0):
            #         gabrielWin = False

        if gabrielWin:
            print >> f, 'Case #%d: GABRIEL' % (i + 1)
        else:
            print >> f, 'Case #%d: RICHARD' % (i + 1)






if __name__ == "__main__":
    main()
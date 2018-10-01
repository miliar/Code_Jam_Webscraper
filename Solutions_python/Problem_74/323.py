def solve(infile):
    input = open(infile)
    T = int(input.readline())
    for t in xrange(1, T+1):
        inputline = input.readline().split()
        N = int(inputline[0])
        result = 0
        robots = {'O' : 1, 'B' : 1}
        last_move = {'O' : 0, 'B' : 0}
        for n in xrange(N):
            R = inputline[n * 2 + 1]
            P = int(inputline[n * 2 + 2])
            since_last_move = result - last_move[R]
            if since_last_move < 0:
                since_last_move = 0
            move_needed = abs(robots[R] - P) - since_last_move
            if move_needed < 0:
                move_needed = 0
            result += move_needed + 1
            robots[R] = P
            last_move[R] = result
        print "Case #%d:" % t, result
    input.close()
    
if __name__ == '__main__':
    import sys
    solve(sys.argv[1])
def read_grid():
    grid = []
    grid.append([int(c) for c in raw_input().split(' ')])
    grid.append([int(c) for c in raw_input().split(' ')])
    grid.append([int(c) for c in raw_input().split(' ')])
    grid.append([int(c) for c in raw_input().split(' ')])
    return grid

sample_count = int(raw_input())
for i in xrange(0, sample_count):
    row1 = int(raw_input())
    # print "row1", row1
    grid1 = read_grid()
    # print "grid1:", grid1
    row2 = int(raw_input())
    # print "row2", row2
    grid2 = read_grid()
    # print "grid2:", grid2
    possible_answers = [n for n in grid1[row1-1] if n in grid2[row2-1]]
    print "Case #%d:" % (i + 1),
    if len(possible_answers) == 1:
        print possible_answers[0]
    elif possible_answers:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"






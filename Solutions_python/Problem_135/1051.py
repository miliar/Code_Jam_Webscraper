#!/usr/bin/python

with open('input.txt', 'r') as inp:

    case_no = 1
    number_of_cases = int(inp.readline())

    for case in range(0, number_of_cases):
        selected_rows = []
        grids = []

        for row in range(0, 2):
            selected_rows.append(int(inp.readline()))

            grid = []
            
            for i in range(0, 4):
                grid.extend([int(val) for val in inp.readline().split(' ')])

            grids.append(grid)

        for grid_a, grid_b in zip(grids[::2], grids[1::2]):

            range_a = grid_a[((selected_rows[0] - 1) * 4):(selected_rows[0] * 4)]
            range_b = grid_b[((selected_rows[1] - 1) * 4):(selected_rows[1] * 4)]

            common_list = list(set(range_a) & set(range_b))

            if len(common_list) > 1:

                print "Case #%d: Bad magician!" % case_no

            elif not common_list:

                print "Case #%d: Volunteer cheated!" % case_no

            else:

                print "Case #%d: %d" % (case_no, common_list[0])

        case_no += 1

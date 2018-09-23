
import sys

def main():

    #  reading in the arguments of the code executable
    fin_name = sys.argv[1]
    fout_name = sys.argv[2]

    # opening the output file for writing
    fout = open(fout_name, 'w')

    #  reading all lines at once from the opened file
    with open(fin_name, 'r') as fin:
        lines = fin.readlines()

    # T - number of test casess
    T = int(lines[0].split()[0])

    ind_line = 0
    for test_case in range(1, T+1):
        
        ind_line += 1
        grid_size = [int(x) for x in lines[ind_line].split()]

        some_row_empty = False
        grid = []

        for row_id in range(grid_size[0]):
            ind_line += 1
            row = [ch for ch in lines[ind_line] if ch != "\n"]
            grid.append(row)

            if not some_row_empty:
                some_row_empty = is_row_empty(row)

        fill_grid(grid, "rows")

        if some_row_empty:

            fill_grid(grid, "columns")


        fout.write("Case #"+str(test_case)+":\n")
        for row in grid:
            fout.write("".join(row)+"\n")

    fin.close()
    fout.close()


def is_row_empty(row):

    if set(row) == {'?'}:
        return True
    else:
        return False

def fill_grid(grid, direction):

    if direction == "rows":
        for row in grid:
            right = 0

            for ch_ind in range(1,len(row)):
                if row[ch_ind] == '?':
                    row[ch_ind] = row[ch_ind-1]

            if row[0] == '?':
                while row[right] == '?':
                    right += 1
                    if right == len(row):
                        break

                if right != len(row):
                    row[0:right], row[right:] = row[right]*(right-1), row[right:]

    else:

        for column in range(len(grid[0])):
            bottom = 0


            for ch_ind in range(1,len(grid)):
                if grid[ch_ind][column] == '?':
                    grid[ch_ind][column] = grid[ch_ind-1][column]

                if grid[0][column] == '?':
                    while grid[bottom][column] == '?':
                        bottom += 1

                    for row in range(bottom):
                        grid[row][column] = grid[bottom][column]

if __name__ == "__main__":
    main()

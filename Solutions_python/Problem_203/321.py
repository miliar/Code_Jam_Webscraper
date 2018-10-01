def main():
    num_cases = int(input())

    for case_num in range(num_cases):
        inp = input().split(' ')
        num_rows = int(inp[0])
        num_cols = int(inp[1])

        grid = []
        for row_num in range(num_rows):
            grid.append(list(input()))

        for row_num in range(num_rows):
            for col_num in range(num_cols):
                if grid[row_num][col_num] != '?':
                    letter = grid[row_num][col_num]
                    new_col = col_num + 1
                    while new_col < num_cols and grid[row_num][new_col] == '?':
                        grid[row_num][new_col] = letter
                        new_col += 1

                    new_col = col_num - 1
                    while new_col >= 0 and grid[row_num][new_col] == '?':
                        grid[row_num][new_col] = letter
                        new_col -= 1

        for row_num in range(num_rows):
            for col_num in range(num_cols):
                if grid[row_num][col_num] != '?':
                    letter = grid[row_num][col_num]
                    new_row = row_num + 1
                    while new_row < num_rows and grid[new_row][col_num] == '?':
                        grid[new_row][col_num] = letter
                        new_row += 1

                    new_row = row_num - 1
                    while new_row >= 0 and grid[new_row][col_num] == '?':
                        grid[new_row][col_num] = letter
                        new_row -= 1

        print("Case #{0}:".format(case_num + 1))
        for row in grid:
            print(''.join(row))


main()

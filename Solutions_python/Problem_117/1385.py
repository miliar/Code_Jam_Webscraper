def main():
    def mowe_row(x,n):
        for i in range(M):
            if gridPossible[x][i] > n:
                gridPossible[x][i] = n
    def mowe_col(y,n):
        for i in range(len(grid)):
            if gridPossible[i][y] > n:
                gridPossible[i][y] = n
    f = open('C:/Users/Rajat/dwhelper/Downloads/B-large.in', 'r')
    g = open('C:/Users/Rajat/dwhelper/Downloads/B-large-out.txt', 'w')
    no_test_cases = int(f.readline())
    for test_case in range(1,no_test_cases+1):
        N, M = f.readline().split()
        N, M = int(N), int(M)
        grid = []
        gridPossible = []
        grid_str = ''
        max_val = 0
        max_val_loc = (0,0)
        do_able = False
        for row in range(N):
            cur_int = []
            str_in = f.readline()
            grid_str += str_in
            cur = str_in.split()
            for i in range(M):
                val = int(cur[i])
                if val > max_val:
                    max_val = val
                    max_val_loc = (row,i)
                cur_int.append(val)
            grid.append(cur_int)
        # Initialising possible grid
        gridPossible = [[max_val for col in range(M)] for row in range(N)]
        # Real Checks..
        if grid_str.count(grid_str[0]) == len(grid_str):
            do_able = True
        else:
            # Construct own grid
            for k in range(N):
                mowe_row(k, grid[k][max_val_loc[1]])
            for l in range(M):
                mowe_col(l, grid[max_val_loc[0]][l])
            if grid == gridPossible:
                do_able = True
        if do_able:
            yes = 'YES'
        else:
            yes = 'NO'
        g.writelines('Case #'+str(test_case)+': '+yes+chr(10))

if __name__ == '__main__':
    main()

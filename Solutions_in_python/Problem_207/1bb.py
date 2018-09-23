def solve(num, r, o, y, g, b, v):
    red = r
    yellow = y
    blue = b

    if red <= yellow + blue and yellow <= red + blue and blue <= red + yellow:
        color = ['R', 'Y', 'B']
        number = [red, yellow, blue]
        f_max = max(number)
        f_idx = number.index(f_max)
        f_col = color.pop(f_idx)
        number.pop(f_idx)
        s_max = max(number)
        s_idx = number.index(s_max)
        s_col = color.pop(s_idx)
        number.pop(s_idx)
        t_max = number[0]
        t_col = color[0]

        overlap = abs(f_max - s_max - t_max)
        res = ''

        f_max -= overlap
        s_max -= overlap
        t_max -= overlap

        color = [f_col, s_col, t_col]
        while overlap > 0:
            for i in range(3):
                res += color[i]
            overlap -= 1

        color = [f_col, t_col]
        while t_max > 0 and f_max > 0:
            for i in range(2):
                res += color[i]
            t_max -= 1
            f_max -= 1

        color = [f_col, s_col]
        while s_max > 0 and f_max > 0:
            for i in range(2):
                res += color[i]
            f_max -= 1
            s_max -= 1
        return res

    else:
        return 'IMPOSSIBLE'



if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        num, r, o, y, g, b, v = [int(s) for s in input().split(" ")]
        result = solve(num, r, o, y, g, b, v)
        print("Case #{}: {}".format(i, result))
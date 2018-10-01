from future.builtins import input
import sys
sys.setrecursionlimit(1500)

IMPOSSIBLE = 'IMPOSSIBLE'

color_map = {
    0: 'R',
    1: 'O',
    2: 'Y',
    3: 'G',
    4: 'B',
    5: 'V',
}


def find_solution2(num, colors, prev_color, start_color):
    # print(num, prev_color, start_color, colors)
    max_num = max(colors)
    max_num_color = colors.index(max_num)

    if num < max_num * 2 - 1:
        return IMPOSSIBLE

    remain_num = num - max_num
    if remain_num == max_num:
        if prev_color == start_color and max_num_color == prev_color:
            return IMPOSSIBLE

    if num <= 1:
        current_color = colors.index(max_num)
        if current_color != prev_color and current_color != start_color:
            return color_map[current_color]
        else:
            return IMPOSSIBLE

    for i in range(6):
        current_color = i
        current_color_num = colors[i]
        if current_color_num >= 1 and current_color != prev_color:
            new_colors = colors.copy()
            new_colors[i] -= 1
            result = find_solution2(num - 1, new_colors, current_color, start_color)
            if result != IMPOSSIBLE:
                return color_map[current_color] + result

    return IMPOSSIBLE

def find_solution(num, colors):
    current_color_num = max(colors)
    current_color = colors.index(current_color_num)
    if current_color_num >= 1:
        new_colors = colors.copy()
        new_colors[current_color] -= 1
        result = find_solution2(num - 1, new_colors, current_color, current_color)
        if result != IMPOSSIBLE:
            return color_map[current_color] + result
    return IMPOSSIBLE

def test():
    test_cases_in = [
        [6, [2, 0, 2, 0, 2, 0]],
        [3, [1, 0, 2, 0, 0, 0]],
        [6, [2, 0, 1, 1, 2, 0]],
        [4, [0, 0, 2, 0, 0, 2]],
        [999, [250, 0, 249, 0, 500, 0]],
    ]
    test_cases_out = [
        'RYBRBY',
        IMPOSSIBLE,
        'YBRGRB',
        'YVYV',
        IMPOSSIBLE,
    ]


    for i in range(len(test_cases_in)):
        solution = find_solution(test_cases_in[i][0], test_cases_in[i][1])
        try:
            assert (solution == test_cases_out[i])
        except:
            print("%d : expected %s, but actual %s" %
                  (i, test_cases_out[i], solution))


# print("---Start Test---")
# test()
# print("---End Test---")

T = int(input())
for t in range(T):
    colors = [int(x) for x in input().split()]
    num = colors.pop(0)
    solution = find_solution(num, colors)
    output_text = "Case #{}: {}".format(t + 1, solution)
    print(output_text)

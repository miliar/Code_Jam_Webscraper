import sys

def order_colors(colors):
    return list(reversed(sorted(range(3), key=lambda i: colors[i])))

assert order_colors([1, 2, 3]) == [2, 1, 0]
assert order_colors([3, 2, 1]) == [0, 1, 2]

def code(color):
    if color == 0:
        return 'R'
    if color == 1:
        return 'Y'
    if color == 2:
        return 'B'

def small(r, y, b):
    colors = [r, y, b]
    previous_color = -1
    result = []
    def push_color(i):
        nonlocal previous_color
        result.append(code(i))
        colors[i] -= 1
        previous_color = i
    if colors[2] > 0:
        push_color(2)
    elif colors[1] > 0:
        push_color(1)
    else:
        push_color(0)
    while True:
        order = order_colors(colors)
        first, second = order[0], order[1]
        if colors[first] == 0:
            if result[0] == result[len(result) - 1]:
                return 'IMPOSSIBLE'
            else:
                return ''.join(result)
        if previous_color != first:
            push_color(first)
        else:
            if colors[second] == 0:
                return 'IMPOSSIBLE'
            push_color(second)

tc_len = int(sys.stdin.readline())

for tc in range(tc_len):
    n, r, o ,y, g, b, v = tuple(int(x) for x in sys.stdin.readline().split())
    assert o == 0
    assert g == 0
    assert v == 0
    print('Case #' + str(tc + 1) + ': ' + small(r, y, b))

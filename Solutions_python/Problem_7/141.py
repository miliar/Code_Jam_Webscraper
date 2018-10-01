def gcomb(x, k):
    "Generate all combinations of k elements from list x."

    if k > len(x):
        return
    if k == 0:
        yield []
    else:
        first, rest = x[0], x[1:]
        # A combination does or doesn't contain first.
        # If it does, the remainder is a k-1 comb of rest.
        for c in gcomb(rest, k-1):
            c.insert(0, first)
            yield c
        # If it doesn't contain first, it's a k comb of rest.
        for c in gcomb(rest, k):
            yield c

def trees(n, A, B, C, D, x0, y0, M):
    X = x0
    Y = y0
    yield X, Y
    for i in xrange(n - 1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        yield X, Y

def count_triangles(n, A, B, C, D, x0, y0, M):
    tree_list = list(trees(n, A, B, C, D, x0, y0, M))
    tree_set = set(tree_list)
    n_triangles = 0
    for p1, p2, p3 in gcomb(tree_list, 3):
        center_x = (p1[0] + p2[0] + p3[0]) / 3.0
        center_y = (p1[1] + p2[1] + p3[1]) / 3.0

        if (center_x == int(center_x) and
            center_y == int(center_y)):
            n_triangles += 1
    return n_triangles

if __name__ == '__main__':
    N = input()
    for i in xrange(N):
        n, A, B, C, D, x0, y0, M = (int(x) for x in raw_input().split())
        print 'Case #%d: %d' % (i + 1,
                                count_triangles(n, A, B, C, D, x0, y0, M))

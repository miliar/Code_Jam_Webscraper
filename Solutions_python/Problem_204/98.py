def num_servings(p, i):
    start = p // i
    lb, ub = None, None
    if 0.9*start*i <= p <= 1.1*start*i:
        lb = start
        _try = lb - 1
        while 0.9*_try*i <= p <= 1.1*_try*i:
            lb = _try
            _try -= 1
    if 0.9*(start+1)*i <= p <= 1.1*(start+1)*i:
        ub = start + 1
        _try = ub + 1
        while 0.9*_try*i <= p <= 1.1*_try*i:
            ub = _try
            _try += 1
    if not lb and ub:
        return ub, ub
    elif not ub and lb:
        return lb, lb
    return lb, ub

def incompatible(ranges):
    min_possible = max(x[0] for x in ranges)
    # print(min_possible)
    for i in range(len(ranges)):
        if ranges[i][1] < min_possible:
            return i
    return None

if __name__ == "__main__":
    cases = int(input())
    for case in range(1, cases+1):
        n, p = map(int, input().split(' '))
        recipe = list(map(int, input().split(' ')))
        packages = []
        for _ in range(n):
            packages.append(sorted(map(int, input().split(' '))))
        ans = 0
        # print(packages)

        while True:
            try:
                current_ranges = []
                for i in range(n):
                    r = (None, None)
                    while r[0] is None:
                        v = packages[i].pop(0)
                        r = num_servings(v, recipe[i])
                    current_ranges.append(r)
                # print(current_ranges)
                im = incompatible(current_ranges)
                # print(im)
                while im is not None:
                    r = (None, None)
                    while r[0] is None:
                        v = packages[im].pop(0)
                        r = num_servings(v, recipe[im])
                    current_ranges[im] = r
                    im = incompatible(current_ranges)
                ans += 1
            except IndexError:
                # print('error')
                break

        print("Case #{}: {}".format(case, ans))

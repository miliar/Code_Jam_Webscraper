def max_googlers(total_points, num_of_surprizing, max_point):
    res = 0
    for total in total_points:
        if max(unsurprizing(total)) >= max_point:
            res += 1
        elif num_of_surprizing > 0 and max(surprizing(total)) >= max_point:
            res += 1
            num_of_surprizing -= 1
    return res

def unsurprizing(total):
    first = total // 3
    second = (total - first) // 2
    third = total - first - second
    _min = min(first, second, third)
    _max = max(first, second, third)
    assert _min >= 0
    assert _max <= 10
    assert _max - _min <= 1
    return sorted([first, second, third])

def surprizing(total):
    first, second, third = unsurprizing(total)
    if first == second and 0 < second < 10:
        first -= 1
        second += 1
    elif second == third and 0 < third < 10:
        second -= 1
        third += 1
    _min = min(first, second, third)
    _max = max(first, second, third)
    assert _min >= 0
    assert _max <= 10
    assert _max - _min <= 2
    return (first, second, third)

with open('/Users/vorushin/Downloads/B-large.in') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
        nums = [int(num) for num in f.readline().split()]
        n, s, p = nums[:3]
        total_points = nums[3:]
        #print n, s, p, total_points
        print 'Case #%d: %d' % (i, max_googlers(total_points, s, p))

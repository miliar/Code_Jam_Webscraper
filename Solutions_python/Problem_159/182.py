def parts(_type=int):
    return map(_type, raw_input().split())

T = int(raw_input())


def a(nums):
    s = 0
    t = nums[0]
    for x in nums[1:]:
        s += max(0, t - x)
        t = x
    return s


def b(nums):
    md = 0
    t = nums[0]
    for x in nums[1:]:
        md = max(md, 0, t - x)
        t = x
    s = 0
    for x in nums[:-1]:
        s += min(x, md)
    return s


for z in range(T):
    N = int(raw_input())
    nums = parts(int)
    print 'Case #{}: {} {}'.format(z + 1, a(nums), b(nums))

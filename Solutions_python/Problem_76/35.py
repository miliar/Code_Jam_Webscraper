def solve(arr):
    nums = [int(c) for c in arr]
    if reduce(lambda a,b: a^b, nums) != 0:
        return 'NO'
    return sum(nums) - min(nums)

with open ('C-large.in') as f:
    t = int(f.readline())
    for i in range(t):
        f.readline()
        arr = f.readline().split(' ')
        print 'Case #{0}: {1}'.format(i+1 ,solve(arr))

import sys
from operator import itemgetter

if __name__=='__main__':
    t = int(sys.stdin.readline())
    for i in range(t):
        sys.stdout.write("Case #{}: ".format(i + 1))
        n = int(sys.stdin.readline())
        nums = map(int, sys.stdin.readline().split(' '))
        ans = 0
        for p in range(n):
            index = min(enumerate(nums), key=itemgetter(1))[0]
            r = len(nums) - 1 - index
            if index < r:
                ans += index
            else:
                ans += r
            nums = nums[:index] + nums[index + 1:]
        sys.stdout.write("{}\n".format(ans))


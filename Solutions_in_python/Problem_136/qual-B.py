import sys

lines = [line for line in sys.stdin]

n_cases = int(lines[0])

class Case:
    def __init__(self, i, c, f, x):
        r = 2.0
        t = 0.0
        while True:
            if x/r > (x/(r+f) + c/r):
                # buy a farm
                t += c/r
                r += f
            else:
                t += x/r
                break
        self.res = "Case #%d: %.8f" % (i, t)
        
    def result(self):
        return self.res

for i in xrange(n_cases):
    nums = lines[i+1].split(' ')
    case = Case(i+1, float(nums[0]), float(nums[1]), float(nums[2]))
    print(case.result())

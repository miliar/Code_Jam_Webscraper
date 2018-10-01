

def is_tidy(num):
    nums = list(str(num))

    # if nums[:-1] == 9:
    #     return True, 0, 0


    length = len(nums)
    i = 1

    for x in reversed(nums):
        next = length - 1 - i
        if next < 0:
            break

        nxt = int(nums[next])
        if int(x) < nxt:
            nums[next] = str(nxt - 1)
            return False, nums, next

        i += 1
    return True, 0, 0


def fillin(nums, i):

    for x in xrange(i, len(nums)):
        nums[x] = '9'

    return ''.join(nums)


def solve(num):
    i = num

    while i > 0:

        tidy, next, fill = is_tidy(i)

        if tidy:
            break

        i = fillin(next, fill + 1)

    if type(i) is str:
        return i.lstrip('0')

    return i


def read_file():
    lines = [line.rstrip('\n') for line in open('C:\Users\Slava\input')]

    target = open('C:\Users\Slava\output', 'w')
    cases = lines[0]

    i = 1
    for x in lines[1:]:

        num = int(x)
        print "Case #{}: {}".format(i, solve(num))
        target.write("Case #{}: {}\n".format(i, solve(num)))
        i += 1

read_file()

# Python 2.6.5

def count(num, a, b):
    s = str(num)
    l = len(s)

    nums = set([])
    for i in range(0, l):
        new_s = s[i:] + s[0:i]
        if (new_s[0] != '0') and (a <= int(new_s)) and (b >= int(new_s)):
            nums.add(new_s)

    return len(nums) - 1


def count_range(a, b):
    result = 0
    for i in range(a, b + 1):
        result += count(i, a, b)
    return result / 2
  

case_num = int(raw_input())

for t in range(1, case_num + 1):
    a, b = map(int, raw_input().split())
    print "Case #%d:" % t, count_range(a, b)

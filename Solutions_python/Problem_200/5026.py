import sys
sys.setrecursionlimit(50000)

def issorted(x, key=lambda x: x):
    return all([key(x[i]) <= key(x[i + 1]) for i in range(len(x) - 1)])


def tidy_num(num):
    tidy = []
    for i in reversed(range(1, num+1)):
        nums = [int(j) for j in str(i)]
        if len(nums) == 1:
            tidy.append(nums)
        if issorted(nums) == True:
            tidy.append(nums)
    return int(''.join(map(str, tidy[0])))

def get_number():
    number = input()
    return int(number)

for i in range(1, 1+get_number()):
    n = get_number()
    sorted_num = tidy_num(n)
    print("Case #{}: {}".format(i, sorted_num))
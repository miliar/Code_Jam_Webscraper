t = int(input())

def is_sorted(x):
    return all(x[i] <= x[i+1] for i in range(len(x)-1))


def solve(num):
    while True:
        num_l = [int(x) for x in str(num)]
        if sorted(num_l) == num_l:
            return num
        else:
            num -= 1

for i in range(1, t+1):
    p = int(input())
    print("Case #{}: {}".format(i, solve(p)))





import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# s = input()

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    n = int(input())
    # last_tiddy = 0
    # for p in range(0, n+1):
    #     if ''.join(sorted(str(p))) == str(p):
    #         last_tiddy = p
    # print(last_tiddy)
    # print("Case #" + str(i) + ": " + str(n) + " " + str(m))

    found = False
    last_tiddy = n
    while not found:
        if ''.join(sorted(str(last_tiddy))) == str(last_tiddy):
            found = True
        else:
            last_tiddy = last_tiddy - 1
    # print(last_tiddy)
    print("Case #{}: {}".format(i, last_tiddy))

# print("Your input is:", s)

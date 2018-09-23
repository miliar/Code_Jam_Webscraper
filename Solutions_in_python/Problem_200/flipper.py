def fix(n, i):
    if n[i] == 1:
        n[i] = 0
        for j in range(i+1, len(n)):
            n[j] = 9
    else:
        n[i] -= 1
        for j in range(i+1, len(n)):
            n[j] = 9

def do_work(n):
    if len(n) == 1:
        return n[0]
    done = False
    while not done:
        done = True
        for i in range(len(n)):
            if i+1 < len(n) and n[i+1] < n[i] and n[i] != 0:
                fix(n, i)
                done = False

    i = 0
    while n[i]==0:
        i += 1
    return int(''.join([str(x) for x in n[i:]]))

# def dumb(n):
#     if len(n) == 1:
#         return n[0]
#     done = False
#     while not done:
#         done = True
#         for i in range(0, len(n)-1):
#             if n[i] > n[i+1]:
#                 n = [int(j) for j in list(str(int(''.join([str(x) for x in n]))-1))]
#                 done = False
#                 break
#     return int(''.join([str(x) for x in n]))





t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = [int(x) for x in list(input())]
    result = do_work(n)
    print("Case #{}: {}".format(i, result))

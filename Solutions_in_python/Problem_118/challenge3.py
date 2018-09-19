import math
T = int(input())


for i in range(T):
    s = set()
    n, m = map(int, input().split())
    for x in range(n, m + 1):
        if str(x) == str(x)[::-1]:
            res = math.sqrt(x)
            if res.is_integer():
                if str(res).split('.')[0] == str(res).split('.')[0][::-1]:
                    s.add(res)
    print('Case #'+ str(i+1) + ': ' + str(len(s)))

# @Author: Tushar Jain <tshrjn>
# @Date:   2017-04-22T21:30:33+05:30
# @Filename: a.py
# @Last modified by:   tshrjn
# @Last modified time: 2017-04-22T22:02:14+05:30



t = int(input())
for i in range(t):
    d, n = list(map(int,input().split()))
    times = []
    for j in range(n):
        k, s = list(map(int,input().split()))
        times.append((d-k)/s)
        # print(k, s)
    # print("max(times)")
    # print(times)
    # print(max(times))
    print("Case #{}: {}".format(i+1 , d/max(times)))

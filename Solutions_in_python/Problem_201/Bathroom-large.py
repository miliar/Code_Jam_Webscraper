import math
t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split(" "))
    longs = 1
    shorts = 0
    twos = math.floor(math.log2(k))
    long_length = n

    for j in range(twos):
        if long_length % 2 == 1:
            longs = 2 * longs + shorts
        else:
            shorts = 2 * shorts + longs
        long_length = math.floor(long_length / 2)

    remaining = int(k - (math.pow(2, twos) - 1))

    if remaining <= longs:
        low = math.floor((long_length-1)/2)
        high = math.ceil((long_length-1)/2)
    else:
        low = math.floor((long_length-2)/2)
        high = math.ceil((long_length-2)/2)

    print("Case #{}: {} {}".format(i, high, low))

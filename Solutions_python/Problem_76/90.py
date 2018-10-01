
def read_ints():
    return map(int, raw_input().split(" "))



def naive(candies, N):
    if reduce(lambda x, y: x ^ y, candies) != 0:
        return -1
    sum = 0
    for i in range(1, (1<<N)-1):
        a = 0
        b = 0
        sa = sb = 0
        for j in range(0, N):
            if (1<<j) & i:
                a ^= candies[j]
                sa += candies[j]
            else:
                b ^= candies[j]
                sb += candies[j]
        if a == b:
            sum = max(sum, sa, sb)
        #print "sa = %d, sb = %d, i = %d" % (sa, sb, i)
    return sum

def large(candies, N):
    if reduce(lambda x, y: x ^ y, candies) != 0:
        return -1
    s = sum(candies)
    return s - min(candies)

T, = read_ints()
for cas in range(T):
    N, = read_ints()
    candies = read_ints()
    
    #ans = naive(candies, N)
    ans = large(candies, N)
    print "Case #%d: %s" % (cas+1, ans == -1 and 'NO' or ans)

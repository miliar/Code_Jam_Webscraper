from math import ceil,sqrt,floor

def is_pal(x):
    sx = str(x)
    if(sx[::-1] == sx):
        return True
    return False

cas = int(raw_input().strip())
for cc in range(1,cas+1):
    inp = raw_input().strip().split()
    a = int(inp[0])
    b = int(inp[1])
    ans = 0
    for i in range(int(ceil(sqrt(a))),int(floor(sqrt(b)))+1):
        if(is_pal(i) and is_pal(i*i)):
            ans += 1
    print 'Case #' + str(cc) + ': ' + str(ans)

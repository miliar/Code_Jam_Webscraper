def maxspeed(des, klist, slist):
    maxtime = 0
    for i in range(len(klist)):
        time = (des-klist[i])/slist[i]
        if (time > maxtime):
            maxtime = time
    return des/maxtime
    

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    d, n = input().split(" ")
    d = int(d)
    n = int(n)
    klist = []
    slist = []
    for j in range(n):
        k, s = input().split(" ")
        k = int(k)
        s = int(s)
        klist.append(k)
        slist.append(s)
    result = maxspeed(d, klist, slist)
    print("Case #{}: {}".format(i, result))

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    D, n = [int(s) for s in input().strip().split()]
    D = float(D)
    maxT = 0
    for j in range(n):
        ki, si = [int(s) for s in input().strip().split()]  # read a list of integers, 2 in this case
        time = 1.0*(D - ki)/si
        maxT = max(maxT, time)
    print("Case #%s: %.6f" % (i, D/maxT))
    # check out .format's specification for more formatting options

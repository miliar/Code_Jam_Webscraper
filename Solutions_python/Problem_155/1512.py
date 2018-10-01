import sys

n = (int) (sys.stdin.readline().strip())
for i in range (1, n+1):
    data = sys.stdin.readline().strip().split(" ")[1]
    total = 0
    add = 0
    for z in range(len(data)):
        if (int) (data[z]) > 0 and z > total:
           add += z - total
           total += z - total
        total += int (data[z])
    print ("Case #{i}: {add}".format(i=i, add = add))

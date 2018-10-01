import math
N = int (raw_input())

file = open("output.txt", "w+")

def write(n, sum1, sum2):
    file.write("Case #%d: %d %d\n" %(n, sum1, sum2))

for i in range(N):
    n = int (raw_input())
    intervals = raw_input().split()
    sum1 = 0
    maxjump = 0
    m = len(intervals) - 1
    for j in range(m):
        if (int (intervals[j]) > int (intervals[j + 1])):
            j = int(intervals[j]) - int (intervals[j+1])
            sum1 += j
            maxjump = max(j, maxjump)
    sum2 = 0
    for j in range(len(intervals)-1):
       sum2 += min(maxjump, int (intervals[j]))
    write(i + 1, sum1, sum2)



import sys

num_case = int(sys.stdin.readline())

for m in range(1, num_case + 1):
# for m in range(1):
    lst = sys.stdin.readline().split()
    A = int(lst[0])
    B = int(lst[1])
    K = int(lst[2])
    
    count = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                count = count + 1
    print("Case #%d: %d" % (m, count))
    
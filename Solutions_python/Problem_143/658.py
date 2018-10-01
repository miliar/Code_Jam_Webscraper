import sys

# - The number of test cases
T = int(sys.stdin.readline())

# - The test case numbers
test_num = 1

while T > 0:
    A, B, K = map(int, sys.stdin.readline().split())
    num_results = 0
    for i in range(0, A):
        for j in range(0, B):
            if i & j < K:
                num_results += 1

    print("Case #%d: %d" %(test_num, num_results))

    T -= 1
    test_num += 1

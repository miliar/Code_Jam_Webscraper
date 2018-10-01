import itertools

testcase_count = int(input())
for testcase_index in range(testcase_count):
    a, b, k = [int(x) for x in input().split()]

##    print(a, b, k)
    result = 0
    for na, nb in itertools.product(range(a), range(b)):
##        print(na, nb)
        if na & nb < k:
            result += 1

    print("Case #%d: %d" % (testcase_index + 1, result))

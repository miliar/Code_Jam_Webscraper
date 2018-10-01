from functools import reduce
import operator as op


def run(case_num):
    n, k = [int(x) for x in input().strip().split()]
    u = float(input())
    cores = [float(x) for x in input().strip().split()]
    cores.sort()
    for i in range(n):
        target = cores[i+1] if i < n-1 else 1.0
        required = target - cores[i]
        to_use = min(required * (i+1), u)
        for j in range(i+1):
            cores[j] += to_use / (i+1)
        u -= to_use
        if u < 0.00001:
            break
    print("Case #{}: {:.8f}".format(case_num, reduce(op.mul, cores)))

for case in range(int(input())):
    run(case+1)

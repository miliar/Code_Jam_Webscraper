from decimal import *
cases = int(input())

all_cases = []

for i in range(cases):
    D, N = [int(i) for i in input().split()]
    list_values = []
    for j in range(N):
        list_values.append(tuple(int(k) for k in input().split()))
    all_cases.append((D, N, list_values))


def max_value(D, N, list_values):
    getcontext().prec = 6
    return D/max([(D-i[0])/i[1] for i in list_values]) + 0.0000001

for i in range(len(all_cases)):
    print("Case #{}: {}".format(i + 1, format(max_value(all_cases[i][0], all_cases[i][1], all_cases[i][2]), '.6f')))

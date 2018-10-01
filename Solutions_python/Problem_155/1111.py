

def solve(max_shyness, distribution):
    result = 0
    n = 0
    for i in range(max_shyness+1):
        if (n < i):
            result += (i - n)
            n = i
        n += distribution[i]
    return result

num_test = int(input())
for i in range(num_test):
    line = input().split()
    print("Case #{0}: {1}".format(i+1, solve(int(line[0]), [int(i) for i in list(line[1])])))

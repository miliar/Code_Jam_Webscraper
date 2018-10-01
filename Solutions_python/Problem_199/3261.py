number_of_tests = int(input())

for test_number in range(number_of_tests):
    pancakes, k = input().split()
    pancakes = list(pancakes)
    k = int(k)
    result = 0
    print("Case #{}: ".format(test_number+1), end='')
    ok = True
    for i in range(len(pancakes)):
        if pancakes[i] == '+':
            continue
        if i+k > len(pancakes):
            ok = False
            break
        result += 1
        for j in range(i, i+k):
            pancakes[j] = '+' if pancakes[j] == '-' else '-'
    if ok:
        print(result)
    else:
        print("IMPOSSIBLE")

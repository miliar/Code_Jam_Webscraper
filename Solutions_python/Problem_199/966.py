import sys

def check_case(pancakes, flipper, i):
    flip = 0
    pancakes_len = len(pancakes)
    for j in range(pancakes_len):
        if pancakes[j]:
            continue
        if flipper + j > pancakes_len:
            print(f"Case #{i}: IMPOSSIBLE")
            return
        flip += 1
        for k in range(flipper):
            pancakes[j+k] = not pancakes[j+k]
    print(f"Case #{i}: {flip}")

n = (int) (sys.stdin.readline().strip())
for i in range (1, n+1):
    data = sys.stdin.readline().split(' ')
    pancakes = [x == "+" for x in data[0]]
    flipper = int(data[1])
    check_case(pancakes, flipper, i)

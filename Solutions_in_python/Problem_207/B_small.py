from math import ceil, floor

def run_test():
    N, R, O, Y, G, B, V = map(int, input().split())
    if O > B or G > R or V > Y:
        return 'IMPOSSIBLE'
    if R > Y + B + G or Y > R + B + V or B > R + Y + O:
        return 'IMPOSSIBLE'
    if R >= Y and R >= B:
        if Y >= B:
            collors = ['R', 'Y', 'B']
            current = [R, Y, B]
        else:
            collors = ['R', 'B', 'Y']
            current = [R, B, Y]
    if Y >= R and Y >= B:
        if R >= B:
            collors = ['Y', 'R', 'B']
            current = [Y, R, B]
        else:
            collors = ['Y', 'B', 'R']
            current = [Y, B, R]
    if B >= R and B >= Y:
        if R >= Y:
            collors = ['B', 'R', 'Y']
            current = [B, R, Y]
        else:
            collors = ['B', 'Y', 'R']
            current = [B, Y, R]

    result = [collors[0] for x in range(current[0])]
    count = 1
    set1 = 0
    set2 = 0
    while set1 < current[1] or set2 < current[2]:
        if set1 < current[1]:
            result.insert(count, collors[1])
            set1 += 1
        elif set2 < current[2]:
            result.insert(count, collors[2])
            set2 += 1
        count += 2
        if count > len(result):
            count = 1

    return ''.join(result)

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))

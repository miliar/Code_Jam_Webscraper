def simulate(num_plates_with_cpy, hiding_point):
    res = 0
    for i in range(1110, hiding_point,-1):
        while num_plates_with_cpy[i] > 0:
            num_plates_with_cpy[i] -= 1
            res += 1
            num_plates_with_cpy[i-hiding_point] += 1

    return res + hiding_point


def solve():
    n = int(input())
    ipt = input()
    diners = [int(x) for x in ipt.split(' ')]
    num_plates_with_cpy = [0 for _ in range(1111)]
    for plate_type in diners:
        num_plates_with_cpy[plate_type] += 1
    result = max(diners)
    for hiding_point in range(1, max(diners)+1):
        result = min(result,
                simulate(num_plates_with_cpy[:], hiding_point))

    return result

if __name__ == '__main__':
    cases = int(input())
    for case in range(1, cases+1):
        print('Case #%d: %s' % (case, str(solve())))

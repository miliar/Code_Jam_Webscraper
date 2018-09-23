import operator
import copy


def check_bad(values):
    if values['R'] > values['B'] + values['G'] + values['Y'] + 1 or \
            values['Y'] > values['B'] + values['R'] + values['V'] + 1 or \
            values['B'] > values['R'] + values['O'] + values['Y'] + 1 or \
            values['G'] > values['R'] + 1 or \
            values['O'] > values['B'] + 1 or \
            values['V'] > values['Y'] + 1:
        return True
    return False


def check_bad_head(result):
    # print(result)
    if result[0] == result[-1] or \
            result[0] == 'R' and result[-1] == 'O' or \
            result[0] == 'R' and result[-1] == 'V' or \
            result[0] == 'Y' and result[-1] == 'O' or \
            result[0] == 'Y' and result[-1] == 'G' or \
            result[0] == 'B' and result[-1] == 'G' or \
            result[0] == 'B' and result[-1] == 'V' or \
            result[0] == 'G' and result[-1] != 'G' or \
            result[0] == 'O' and result[-1] != 'O' or \
            result[0] == 'V' and result[-1] != 'V':
        return True
    return False


def check_bad_first(values):
    if values['R'] > values['B'] + values['G'] + values['Y'] + 1 or \
            values['Y'] > values['B'] + values['R'] + values['V'] + 1 or \
            values['B'] > values['R'] + values['O'] + values['Y'] + 1 or \
            values['G'] > values['R'] + 1 or \
            values['O'] > values['B'] + 1 or \
            values['V'] > values['Y'] + 1:
        return True
    return False


def sim(values, key):
    temp = copy.deepcopy(values)
    temp[key] -= 1
    return temp


t = int(input())

for i in range(1, t + 1):
    [N, R, O, Y, G, B, V] = [int(s) for s in input().split(" ")]

    values = {'R': R, 'O': O, 'Y': Y, 'G': G, 'B': B, 'V': V}
    values_orig = copy.deepcopy(values)
    maxx = 0
    max_keys = []
    for key in values:
        if values[key] > maxx:
            maxx = values[key]
    for key in values:
        if values[key] == maxx:
            max_keys.append(key)

    # print(max_keys)

    for max_key in max_keys:
        # print('max:', max_key)
        values = copy.deepcopy(values_orig)
        if check_bad_first(values):
            result = 'IMPOSSIBLE'
        else:
            result = ''

        for n in range(int(N)):
            if check_bad(values):
                result = 'IMPOSSIBLE'
                break
            if sum(values.values()) == 0:
                break
            if result == '':
                result += max_key
                values[max_key] -= 1
            elif result[-1] == 'G':
                result += 'R'
                values['R'] -= 1
            elif result[-1] == 'V':
                result += 'Y'
                values['Y'] -= 1
            elif result[-1] == 'O':
                result += 'B'
                values['B'] -= 1
            elif result[-1] == 'R' and values['G'] != 0:
                result += 'G'
                values['G'] -= 1
            elif result[-1] == 'Y' and values['V'] != 0:
                result += 'V'
                values['V'] -= 1
            elif result[-1] == 'B' and values['O'] != 0:
                result += 'O'
                values['O'] -= 1
            elif result[-1] == 'R':
                if check_bad(sim(values, 'B')) and check_bad(sim(values, 'Y')):
                    result = 'IMPOSSIBLE'
                    break
                elif not check_bad(sim(values, 'B')) and not check_bad(sim(values, 'Y')) and values['B'] != 0 and values['Y'] != 0:
                    if values['B'] > values['Y']:
                        result += 'B'
                        values['B'] -= 1
                    elif values['Y'] > values['B']:
                        result += 'Y'
                        values['Y'] -= 1
                    elif check_bad_head(result + 'Y'):
                        result += 'Y'
                        values['Y'] -= 1
                    else:
                        result += 'B'
                        values['B'] -= 1
                elif check_bad(sim(values, 'B')) and values['Y'] != 0:
                    result += 'Y'
                    values['Y'] -= 1
                elif values['B'] != 0:
                    result += 'B'
                    values['B'] -= 1
            elif result[-1] == 'Y':
                if check_bad(sim(values, 'R')) and check_bad(sim(values, 'B')):
                    result = 'IMPOSSIBLE'
                    break
                elif not check_bad(sim(values, 'R')) and not check_bad(sim(values, 'B')) and values['R'] != 0 and values['B'] != 0:
                    if values['R'] > values['B']:
                        result += 'R'
                        values['R'] -= 1
                    elif values['B'] > values['R']:
                        result += 'B'
                        values['B'] -= 1
                    elif check_bad_head(result + 'R'):
                        result += 'R'
                        values['R'] -= 1
                    else:
                        result += 'B'
                        values['B'] -= 1
                elif check_bad(sim(values, 'R')) and values['B'] != 0:
                    result += 'B'
                    values['B'] -= 1
                elif values['R'] != 0:
                    result += 'R'
                    values['R'] -= 1
            elif result[-1] == 'B':
                if check_bad(sim(values, 'R')) and check_bad(sim(values, 'Y')):
                    result = 'IMPOSSIBLE'
                    break
                elif not check_bad(sim(values, 'R')) and not check_bad(sim(values, 'Y')) and values['R'] != 0 and values['Y'] != 0:
                    if values['R'] > values['Y']:
                        result += 'R'
                        values['R'] -= 1
                    elif values['Y'] > values['R']:
                        result += 'Y'
                        values['Y'] -= 1
                    elif check_bad_head(result + 'Y'):
                        result += 'Y'
                        values['Y'] -= 1
                    else:
                        result += 'R'
                        values['R'] -= 1
                elif check_bad(sim(values, 'R')) and values['Y'] != 0:
                    result += 'Y'
                    values['Y'] -= 1
                elif values['R'] != 0:
                    result += 'R'
                    values['R'] -= 1

        if check_bad_head(result):
            result = 'IMPOSSIBLE'
        if len(result) < int(N):
            result = 'IMPOSSIBLE'
        if result != 'IMPOSSIBLE':
            break

    print("Case #{}: {}".format(i, result))

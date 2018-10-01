def main():
    t = int(input())
    cases = []
    for i in range(0, t):
        line = input()
        case = line.split()
        pancakes = list(case[0])
        k = int(case[1])
        cases.append([pancakes, k])
    case_num = 1

    for case in cases:
        num_flips = 0
        pancakes = case[0]
        k = case[1]
        for i in range(0, len(pancakes) - k + 1):
            if pancakes[i] == '+':
                continue
            else:
                for j in range(0, k):
                    index = i + j
                    pancakes[index] = flip(pancakes[index])
                num_flips += 1

        if '-' in pancakes[-k:]:
            print("Case #{0}: IMPOSSIBLE".format(case_num))
        else:
            print("Case #{0}: {1}".format(case_num, num_flips))
        case_num += 1

def flip(pancake):
    if pancake == '+':
        return '-'
    else:
        return '+'

main()

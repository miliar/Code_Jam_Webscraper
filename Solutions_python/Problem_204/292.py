import sys


def solve(recipe, quantities, case_number):
    indexes = [0] * len(quantities)
    count = 0
    for i in range(0, len(quantities[0])):
        max_kits = int((quantities[0][i] / 0.9) / recipe[0])
        min_kits = int((quantities[0][i] / 1.1) / recipe[0])
        for kits in range(min_kits, max_kits + 1):
            if recipe[0] * kits * 1.1 < quantities[0][i] or recipe[0] * kits * 0.9 > quantities[0][i]:
                continue
            for j in range(1, len(quantities)):
                original = indexes[j]
                for k in range(indexes[j], len(quantities[0])):
                    if recipe[j] * kits * 1.1 < quantities[j][k] or recipe[j] * kits * 0.9 > quantities[j][k]:
                        continue
                    indexes[j] = k + 1
                    break
                else:
                    indexes[j] = original
                    break
            else:
                count += 1
                break

    print("Case #%d: %d" % (case_number, count))


def main():
    f = sys.stdin
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')

    total_cases = f.readline()
    for case_number in range(1, int(total_cases) + 1):
        n, p = map(int, f.readline().strip().split(' '))
        recipe = map(int, f.readline().strip().split(' '))
        quantities = []
        for _ in range(0, n):
            quantities.append(sorted(map(int, f.readline().strip().split(' '))))

        solve(recipe, quantities, case_number)


if __name__ == "__main__":
    main()

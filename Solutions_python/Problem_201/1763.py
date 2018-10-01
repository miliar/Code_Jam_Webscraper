# Problem C


def solve(n, k):
    empty_list = list()
    empty_list.append(n)

    for idx in range(k):
        empty_max = max(empty_list)
        empty_list.remove(max(empty_list))

        empty_stall = empty_max - 1
        if empty_stall <= 0:
            return 0, 0
        empty_half = int(empty_stall / 2)
        empty_max = empty_half
        empty_min = empty_half

        if empty_stall % 2 == 1:
            empty_max += 1

        empty_list.append(empty_max)
        empty_list.append(empty_min)

    return empty_max, empty_min


def main():
    inputFile = "C-small-1-attempt3.in"
    #inputFile = "C-large.in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    test_case = int(inpf.readline())

    #false_msg = "IMPOSSIBLE"

    for case in range(test_case):

        n, k = [int(x) for x in inpf.readline().strip().split(' ')]
        ma, mi = solve(n, k)

        result = 'Case #{}: {} {}\n'.format(case + 1, ma, mi)

        print(result, end='')
        outf.write(result)
    inpf.close()
    outf.close()





if __name__ == "__main__":
    main()
    #ma, mi = solve(6, 2)
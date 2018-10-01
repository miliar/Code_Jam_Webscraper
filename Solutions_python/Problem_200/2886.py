import sys

def solve(number):
    for i in range(len(number) - 2, -1, -1):
        if number[i] > number[i + 1]:
            number[i] = number[i] - 1
            number[i + 1:] = [9] * (len(number) - i - 1)
        print(number)
    return "".join([str(n) for n in number if n != 0])


def main():
    f = open(sys.argv[1])
    f_out = open(sys.argv[2], 'w')
    tests = int(f.readline())
    for i in range(0, tests):
        number = f.readline()
        number = [int(n) for n in number.strip()]
        f_out.write("Case #{}: {}\n".format(i + 1, solve(number)))


if __name__ == "__main__":
    main()
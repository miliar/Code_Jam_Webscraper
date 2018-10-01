import fileinput

def check_for_tidy(number):
    tidy = all([int(number[i]) <= int(number[i + 1]) for i in range(len(number) - 1)])
    return tidy

def make_int(number):
    return int(number.replace("0",""))

def find_last_tidy(number):
    if check_for_tidy(number):
        return make_int(number)

    for i in range(len(number) - 1):
        if int(number[i]) > int(number[i + 1]):
            decrease_end = i
            break
    decrease_start = decrease_end
    for i in range(decrease_end - 1, -1, -1):
        if number[i] == number[decrease_end]:
            decrease_start = i
        else:
            break
    start = number[:decrease_start]
    middle = str(int(number[decrease_end]) - 1)
    end = ""
    for i in range(decrease_start + 1, len(number)):
        end += "9"

    tidy = make_int(start + middle + end)
    return tidy


def main():
    file = fileinput.input()
    n = int(file.readline())
    for i in range (1, n + 1):
        number = file.readline().replace("\n", "")
        last_tidy = find_last_tidy(number)
        print "Case #%d: %d" % (i, last_tidy)


if __name__ == "__main__":
    main()

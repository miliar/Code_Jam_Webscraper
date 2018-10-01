def reduce(num, i):
    if num == ["0"] * len(num):
        return num
    if num[i] != "0":
        num[i] = str(int(num[i]) - 1)
        for j in range(-1, i, -1):
            num[j] = "9"
        return num
    else:
        reduce(num, i - 1)
        return num


def tidy_numbers():
    test_cases = int(input().strip())
    for test_case in range(test_cases):
        num = list(input().strip())
        while True:
            sorted_num = sorted(num)
            if sorted_num == num:
                for i in range(len(sorted_num)):
                    if sorted_num[i] == "0":
                        sorted_num = sorted_num[i+1:]
                    else:
                        break
                print("Case #" + str(test_case + 1) + ": " + "".join(sorted_num))
                break
            num = reduce(num, -1)

tidy_numbers()
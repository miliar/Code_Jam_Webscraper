#returns string: minimum # flips (if possible)
# n: pancake sequence (+/-), size of flipper
def solve(input):
    pancakes = input.split()[0]
    pancakes_list = list(pancakes)
    size = int(input.split()[1])
    result = 0

    for i in range(0, (len(pancakes)-(size-1))):
        if pancakes_list[i] == "-": #flip
            for j in range(i, i+size):
                if (pancakes_list[j] == "-"):
                    pancakes_list[j] = "+"
                else:
                    pancakes_list[j] = "-"
            result += 1

    for x in pancakes_list:
        if x == "-":
            return "IMPOSSIBLE"
    return str(result)

if __name__ == "__main__":
    test_case_num = raw_input()
    for i in range(1, int(test_case_num)+1):
        input = raw_input()
        result = solve(input)
        print("Case #" + str(i) + ": " + result)

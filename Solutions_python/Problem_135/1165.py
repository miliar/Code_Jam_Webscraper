num_cases = int(raw_input())

for case in range(1, num_cases + 1):
    ans1 = int(raw_input())

    for i in range(1, 5):
        read = raw_input()
        if i == ans1:
            row1 = read.split(" ")
            row1 = set([int(r) for r in row1])

    ans2 = int(raw_input())

    for i in range(1, 5):
        read = raw_input()
        if i == ans2:
            row2 = read.split(" ")
            row2 = set([int(r) for r in row2])

    common = row1.intersection(row2)

    num = len(common)

    if num == 1:
        output = str(common.pop())
    elif num < 1:
        output = "Volunteer cheated!"
    else:
        output = "Bad magician!"

    print ("Case #" + str(case) + ": " + output)
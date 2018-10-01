# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
F = open("tidy-result.in", 'w')
for i in range(1, t + 1):
    init_num = int(input())
    init_num_1 = int(init_num % 10**9)
    init_num_2 = int(init_num // 10 ** 9)
    num1_okay = False
    if init_num_2 > 0:
        num2_okay = False
    else:
        num2_okay = True
    while True:
        num = init_num_1
        least = 10
        while num > 0:
            if least >= num % 10:
                least = num % 10
                num1_okay = True
            else:
                num1_okay = False
                break
            num = num // 10

        num = init_num_2
        while num > 0:
            if least >= num % 10:
                least = num % 10
                num2_okay = True
            else:
                num2_okay = False
                break
            num = num // 10
        if(not num1_okay or not num2_okay):
            init_num_1 -= 1
            if init_num_1 < 0:
                init_num_2 -= 1
                init_num_1 = 10**9 -1
        else:
            break
    if init_num_2 > 0:
        final_num = str(init_num_2) + str(init_num_1)
    else:
        final_num = str(init_num_1)
    print("Case #{}: {}\n".format(i, final_num))
    F.write("Case #{}: {}\n".format(i, final_num))
    # check out .format's specification for more formatting options

F.close()
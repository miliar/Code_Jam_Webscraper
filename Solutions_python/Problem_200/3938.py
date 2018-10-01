# cd F:\pythonscripts\Code_jam

def order():
    lines = [int(i) for i in tuple(open("B-large.in", 'r'))]
    testcases = lines[0]
    lines = lines[1:]


    num_changer = {i:i-1 for i in range(1, 10)}
    num_changer[0] = 9
    for testcase in range(1, testcases+1):
        case = "Case #{}: ".format(testcase)

        n = lines[testcase-1]
        n_list = [int(i) for i in list(str(n))]
        n_list.reverse()

        for index, num in enumerate(n_list):
            try:
                next_num = n_list[index+1]
                if num < next_num:
                    n_list[index] = num_changer[num]
                    n_list[index+1] = num_changer[next_num]
            except IndexError:
                pass
        n_list.reverse()

        # Use zero buffering to lower the number by powers of 10
        n_list = int(''.join([str(i) for i in n_list]))

        n_list = [int(i) for i in list(str(n_list))]

        for index, num in enumerate(n_list):
            try:
                next_num = n_list[index+1]
                if num > next_num:
                    n_list[index+1] = 9
            except IndexError:
                pass

        answer = int(''.join([str(i) for i in n_list]))

        with open("answer.txt", "a") as f:
            f.writelines("{}{}\n".format(case, answer))
            f.close()


if __name__ == '__main__':
    order()

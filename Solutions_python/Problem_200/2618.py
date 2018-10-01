CASE_FMT = "Case #{}: {}"
DBG = False


def dbg(mess):
    if DBG:
        print("_ {}".format(mess))


def is_tidy(num):
    s_num = str(num)
    for i in range(len(s_num) - 1):
        if int(s_num[i]) > int(s_num[i + 1]):
            return False
    return True


def gen_lower_tidy(num):
    s_num = list(str(num))
    lower = False
    dbg(s_num)
    for j in range(len(s_num) - 1, 0, -1):
        dbg("{}: {} ? {}".format(j, s_num[j - 1], s_num[j]))
        if lower:
            if int(s_num[j]) > 0:
                s_num[j] = str(int(s_num[j]) - 1)
                lower = False
            else:
                s_num[j] = '9'
                lower = True
        if int(s_num[j - 1]) > int(s_num[j]):
            s_num[j] = '9'
            lower = True
        elif int(s_num[j - 1]) <= int(s_num[j]):
            edit = False
            for k in range(j - 1, 0, -1):
                if int(s_num[k - 1]) > int(s_num[k]):
                    edit = True
                    break
            if edit:
                s_num[j] = '9'
                lower = True
    if lower:
        s_num[0] = str(int(s_num[0]) - 1)
    return int(''.join(s_num))


if __name__ == "__main__":
    n = int(input())
    for i in range(1, n + 1):
        limit = int(input())
        j = gen_lower_tidy(limit)
        print(CASE_FMT.format(i, j))

        # for j in range(limit, 1, -1):
        #     # dbg("{} {}".format(j, is_tidy(j)))
        #     # if is_tidy(j):
        #     #     print(CASE_FMT.format(i, j))
        #     #     break
        #     # else:
        #
        #     break

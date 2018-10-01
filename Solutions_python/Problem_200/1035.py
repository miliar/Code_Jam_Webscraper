def is_tidy(num):
    str_num = str(num)
    for i in range(len(str_num)-1):
        if int(str_num[i]) > int(str_num[i+1]):
            return False
    return True


def main():
    n = int(raw_input().strip())

    for case_num in range(n):
        num = int(raw_input().strip())
        while not is_tidy(num):
            str_num = str(num)
            str_num_list = list(str_num)
            for i in range(len(str_num_list)-1):
                if int(str_num_list[i]) > int(str_num_list[i+1]):
                    digit_num = int(str_num_list[i])
                    str_num_list[i] = str(digit_num - 1)
                    for j in range(i+1, len(str_num_list)):
                        str_num_list[j] = '9'
            num = int(''.join(str_num_list))

        print 'Case #{}: {}'.format(case_num+1, num)


if __name__ == '__main__':
    main()

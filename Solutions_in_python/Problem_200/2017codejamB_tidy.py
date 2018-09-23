T = int(input())

def check_tidy(x):
    len_x = len(x)
    cur_num = int(x[0])
    for i in range(len_x - 1):
        next_num = int(x[i+1])
        if cur_num > next_num:
            return i
        cur_num = next_num
    return -1

def biggest_num(x):
    tidy_index = check_tidy(x)
    if x == "0":
        return ""
    if check_tidy(x) == -1:
        return x
    else:
        return biggest_num(str(int(x[:tidy_index+1])-1)) + "9" * (len(x)- tidy_index - 1)

for t in range(1, T+1):
    str_N = input()
    print("Case #" + str(t) + ": " + biggest_num(str_N))
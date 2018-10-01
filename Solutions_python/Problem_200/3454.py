import sys

def get_tidy(val):
    list_val = list(str(val))
    if(len(list_val) == 1): return val

    wrong_digit = 0 # start from first digit
    #print val
    # digits needs to be reset if first iteration does not result in
    # tidy number
    #print  val


    while(list_val[wrong_digit] <= list_val[wrong_digit+1]):
        wrong_digit += 1
        if(wrong_digit == (len(list_val) - 1)):
            return val

    while(list_val[wrong_digit - 1] == list_val[wrong_digit]):
        if(wrong_digit == 0): break
        wrong_digit -= 1

    list_val[wrong_digit] = str(int(list_val[wrong_digit]) - 1)
    #print wrong_digit
    for index in range(0, len(list_val) - wrong_digit -1):
        list_val[len(list_val) - index - 1] = '9'
    #print list_val
    return int("".join(list_val))

input_count = int(raw_input())
index = 1
while (input_count > 0):
    cur_line = int(raw_input())
    sys.stdout.write("Case #{}: {}\n".format(str(index), get_tidy(cur_line)))
    input_count -= 1
    index += 1

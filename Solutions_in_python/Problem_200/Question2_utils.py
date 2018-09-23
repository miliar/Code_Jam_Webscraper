def find_tidy(num):
    if int(num) < 10:
        return num
    
    index = len(num) - 2
    for i in range(0, len(num) - 1):
        # power = 1
        while(index >= 0):
            if num[1:].count('0') is len(num[1:]):
                return str(int(num) - 1)

            if num[index] > num[index + 1]:
                need_to_minus = int(num[index+1:]) + 1
                # print("Need to minus " + str(need_to_minus))
                num = str(int(num) - need_to_minus)

            index -= 1
            # power *= 10
    return num
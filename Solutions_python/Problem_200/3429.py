import os

f = open('B-large.in.txt')
cases = int(f.readline())
strs = []
numbers = []
results = []

for _ in range(0, cases + 1):
    string = f.readline().strip()
    # strs.append(str.trim())
    if string.isdigit():
        numbers.append(int(string))

for number in numbers:
    # for i in range(number,0,-1):
    #     i_str = str(i)
    #     i_str_ordered = sorted([j for j in i_str])
    #     i_ordered = int("".join(i_str_ordered))
    #     if i == i_ordered:
    #         results.append(i)
    #         break

    i_str = str(number)
    digits = [j for j in i_str]
    if len(digits) == 1:
        results.append(number)
    else:
        for ii, d in enumerate(digits):
            if ii < len(digits) - 1:
                if d > digits[ii + 1]:
                    # generate the maximum possible number
                    if ii == 0:
                        if int(d) > 1:
                            num_str = []
                            num_str.append(str(int(d) - 1))
                            for _ in range(1, len(digits)):
                                num_str.append(str(9))
                            num = int("".join(num_str))
                            results.append(num)
                            break
                        else:
                            num_str = []
                            for _ in range(1, len(digits)):
                                num_str.append(str(9))
                            num = int("".join(num_str))
                            results.append(num)
                            break
                    else:
                        if d > digits[ii - 1]:
                            num_str = []
                            for j in range(0, ii):
                                num_str.append(str(digits[j]))
                            num_str.append(str(int(d) - 1))
                            for _ in range(ii + 1, len(digits)):
                                num_str.append(str(9))
                            num = int("".join(num_str))
                            results.append(num)
                            break
                        else:
                            index = ii - 2
                            while d == digits[index] and index >= 0:
                                index -= 1
                            if index < 0:
                                num_str = []
                                if digits[0] != 1:
                                    num_str.append(str(int(digits[0])-1))
                                for _ in range(1, len(digits)):
                                    num_str.append(str(9))
                                num = int("".join(num_str))
                                results.append(num)
                                break
                            else:
                                num_str = []
                                for k in range(0,index+1):
                                    num_str.append(str(int(digits[k])))
                                num_str.append(str(int(digits[index+1])-1))
                                for _ in range(index+2, len(digits)):
                                    num_str.append(str(9))
                                num = int("".join(num_str))
                                results.append(num)
                                break


                        print()
        # if the number is in order, add the number itself
            if ii == len(digits) - 1:
                results.append(number)


f2 = open('output2.large.txt', 'w')
for i, result in enumerate(results):
    f2.write("Case #{}: {}\n".format(i + 1, result))
f2.close()

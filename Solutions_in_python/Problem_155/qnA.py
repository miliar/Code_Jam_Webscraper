i = open('A-large.in')
o = open('out.txt', 'w')

num = i.readline()
num = int(num)

for x in range(1, num + 1):
    x = str(x)
    num2 = i.readline()
    num2 = num2.split()
    audience = num2[1]
    list_of_digits = []
    for each in audience:
        each = int(each)
        list_of_digits.append(each)
    min_num = 0
    for member in range(len(list_of_digits) - 1):
        if list_of_digits[member] == 0:
            if member == 0:  # if there are no audience members with shyness level 0
                min_num += 1
                list_of_digits[0] = 1
            else:
                count = 0
                counter = 1
                while member - counter >= 0: # running backwards through the list
                    count += list_of_digits[member - counter] # calculate total standing audience
                    counter += 1
                counter2 = 0
                while list_of_digits[member + counter2] == 0:  # if there are consecutive zeroes; checking which is the next non-zero integer
                    counter2 += 1
                if count >= member + counter2: # if standing audience is greater than necessary to get remaining to stand
                    pass
                else: # if not enough
                    min_num += 1
                    list_of_digits[member] = 1
    o.write("Case #" + x + ": " + str(min_num) + "\n")
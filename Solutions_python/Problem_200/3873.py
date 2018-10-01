import sys
def opti (num):

    string = str(num)
    stack = 0
    for index in range(len(string)- 1):
        if string[index] > string[index + 1]:
            if stack != 0:
                return [string[:stack_index], string[stack_index:]]

            return [string[:index], string[index:]]

        elif string[index] == string[index + 1]:
            stack += 1
            if stack == 1:
                stack_index = index
        else:
            fine_index = index

    return [string[:]]

def solver(num):
    list_output = opti(num)

    if len(list_output) == 1:
        return_num = int(list_output[0])

    else:
        first_num = 0
        second_num = 0
        if list_output[0] != '':
            first_num = int(list_output[0])
        if list_output[1] != '':
            second_num = int(list_output[1])

        first = str(second_num)
        first = int(first[0]) - 1
        first = str(first)

        for x in range (len(str(second_num)) - 1):
            first = first + '9'

        return_num = int(str(first_num) + first)

    return return_num

input_file = sys.argv[1] + '.in'
output_file = sys.argv[1] + '.out'
def parser(input_file):
    with open (input_file) as fin:
        fix = fin.read().split('\n')
        biglist = [line.strip().split(' ') for line in fix]
        biglist = biglist[1:-1]

        return biglist

return_list = []
biglist = parser(input_file)



for element in biglist:
    testnum = int(element[0])
    print (element)
    return_list.append(solver(testnum))

def outputer(output_file, list):
    with open (output_file, 'w') as out:
        x = 1
        for element in return_list:
            out.write('Case #%d: %d \n' % (x, element) )

            x += 1

outputer(output_file, biglist)

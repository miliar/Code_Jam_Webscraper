fo = open("input.txt", 'r')
fi = open("output_big.txt",'w')
input = []

for i in fo:
    input.append(i)

del(input[0])

test_case_number = 1
answer = []
numbers = input
####################################################################


def is_tidy(x):
    x = list(str(x))
    for i in range(0,len(x)-1):
        if x[i]>x[i+1]:
            return False
    return True

#print ('numbers: ', numbers[1].split()[0])

for number in numbers:
    iteration = len(number)
    tmp_2 = ''
    #print '---->number: ',number
    number = number.split()[0]
    tmp_1 = number

    for i in range(0,iteration):

        if is_tidy(tmp_1):
            answer.append('Case #'+str(test_case_number)+': ' + str(tmp_1))
            break

        tmp_1 =  tmp_1[:-1]
        #print 'tmp_1: ',tmp_1
        tmp_2 = tmp_2 + '9'
        #print 'tmp_2', tmp_2
        tmp_1 = int(tmp_1) - 1
        tmp_1 = str(tmp_1)
        if tmp_1 != '0':
            tmp_3 = tmp_1 + tmp_2
        else:
            tmp_3 = tmp_2
        #print 'tmp_3', tmp_3
        #print 'tmp3: ', tmp_3
        if is_tidy(tmp_3):
            answer.append('Case #'+str(test_case_number)+': ' + str(tmp_3))
            break

    test_case_number = test_case_number + 1


###############################################################
for i in answer:
    #print i
    fi.write(str(i) + ' \n')

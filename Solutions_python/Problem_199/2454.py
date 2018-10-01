fo = open("input.txt", 'r')
fi = open("output.txt",'w')
input = []

for i in fo:
    input.append(i)

del(input[0])

def flip(x):
    if x == '+':
        return '-'
    elif x == '-':
        return '+'

test_case_number = 1
answer = []
for par in input:
    pan_cake = par.split()[0]
    flipper_size = int(par.split()[1])
    pan_cake = list(pan_cake)
    counter = 0
    impossible = False


    for i in range(len(pan_cake)):
        if(pan_cake[i] == '-'):
            j=i
            counter = counter +1
            if(j+flipper_size<=len(pan_cake)):
                for j in range(j,flipper_size+j):
                    pan_cake[j] = flip(pan_cake[j])

    for i in pan_cake:
        if(i=='-'):
            impossible = True;
            break

    if(impossible==True):
        answer.append(str('Case #'+str(test_case_number)+': '+'IMPOSSIBLE'))
    else:
        answer.append('Case #'+str(test_case_number)+': ' + str(counter))
    test_case_number += 1


for i in answer:
    #print i
    fi.write(i + ' \n')

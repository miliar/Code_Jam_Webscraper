
f = open('C-small-attempt3.in', 'r')
x = f.read().split('\n')
f.close()
L = []
# reading the file:
x.pop(0)
if x.__contains__(''):
    x.remove('')
count = 0
for i in x:
    if i.isalpha():
        y = x[count-1].split(" ")
        string = i*int(y[1])
        L.append(string)
    count = count + 1


# the matrix
D = {('1', '1'): '1', ('1', 'i'): 'i', ('1', 'j'): 'j', ('1', 'k'): 'k', ('i', '1'): 'i',
     ('i', 'i'): '-1', ('i', 'j'): 'k', ('i', 'k'): '-j', ('j', '1'): 'j', ('j', 'i'): '-k',
     ('j', 'j'): '-1', ('j', 'k'): 'i', ('k', '1'): 'k', ('k', 'i'): 'j', ('k', 'j'): '-i', ('k', 'k'): '-1'}
Result = []


def k_sub(i):
    flag = False
    index = -1
    string = ''
    if i[index] == 'k':
        flag = True

    while index >= (-1*(len(i)-1)) and not flag:

        if string != '' and not flag:
            if len(string) > 1:
                p_string = D[(i[index], string[1])]
                if len(p_string) > 1:
                    string = p_string[1]
                else:
                    string = '-'+p_string
            else:
                string = D[(i[index], string)]
            if string == 'k':
                flag = True
                break
            index = index - 1
        elif string == '':
            string = D[(i[index-1], i[index])]
            index = -3
    return index, flag


def i_sub(i):
    flag = False
    index = 0
    string = ''
    if i[index] == 'i':
        flag = True

    while index <= (len(i)-1) and not flag:
        if string != '' and not flag:
            if len(string) > 1:
                p_string = D[(string[1], i[index])]
                if len(p_string) > 1:
                    string = p_string[1]
                else:
                    string = '-'+p_string
            else:
                string = D[(string, i[index])]

            if string == 'i':
                flag = True
                break

            index = index + 1

        elif string == '':
            string = D[(i[index], i[index+1])]
            index = 2
    return index, flag


def j_sub(i):
    flag = False
    index = 0
    string = ''
    while index <= len(i)-1:
        if string != '' and not flag:
            if len(string) > 1:
                p_string = D[(string[1], i[index])]
                if len(p_string) > 1:
                    string = p_string[1]
                else:
                    string = '-'+p_string
            else:
                string = D[(string, i[index])]

            index = index + 1

        elif string == '' and len(i) > 1:
            string = D[(i[index], i[index+1])]
            index = 2
        elif string == '' and len(i) <= 1:
            if i[0] == 'j':
                flag = True
                index = 1
                break
    if string == 'j':
        flag = True
    return index, flag

for i in L:
    i = list(i)
    k_d = k_sub(i)
    len_k = k_d[0]
    if len(i) == -1*k_d[0] and k_d[1]:
        # not possible to create sub string.
        Result.append("NO")
    elif (len(i)-(-1*k_d[0])) < 2 and k_d[1]:
        # then no other string is possible to create i,k
        Result.append("NO")
    elif k_d[1]:
        # we can search for i now.
        i_d = i_sub(i)
        i = i[i_d[0]+1:len_k]
        print i
        if i and i_d[1]:
            # we can check if the last segment can reduce to j.
            j_d = j_sub(i)
            if j_d[0] == len(i) and j_d[1]:
                # we can reduce to ijk
                Result.append("YES")
            else:
                Result.append("NO")
        else:
            Result.append("NO")
    else:
        Result.append("NO")
print Result


# writing the results to file
f = open('file.out', 'w')
j = 1
for i in Result:
    f.write('Case #' + str(j) + ': ' + i) # python will convert \n to os.linesep
    f.write('\n')
    j=j+1
f.close()

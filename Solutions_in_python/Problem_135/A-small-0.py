f = open('A-small-0.in', 'r')
f2 = open('A-small-0.out', 'w')

t = f.readline()

case_num = 1

for x in range(int(t)):
    initial_row = f.readline()
    initial_row_vals = []
    for i in range(int(initial_row)):
        initial_row_vals = f.readline().split()
    for i in range((4 - int(initial_row))):
        f.readline()

    print(initial_row_vals)

    second_row = f.readline()
    second_row_vals = []
    for i in range(int(second_row)):
        second_row_vals = f.readline().split()
    for i in range((4 - int(second_row))):
        f.readline()

    print(second_row_vals)

    flag = -1
    count = 0
    for i in range(len(initial_row_vals)):
        for j in range(len(second_row_vals)):
            if int(initial_row_vals[i]) == int(second_row_vals[j]):
                flag = initial_row_vals[i]
                count = count + 1

    print(flag)
    print(count)
            
    if(flag != -1 and count == 1):
        f2.write('Case #' + str(case_num) + ': ' + str(flag) + '\n')
        print('Case #' + str(case_num) + ': ' + str(flag) + '\n')
    elif(flag != -1 and count > 1):
        f2.write('Case #' + str(case_num) + ': Bad magician!' + '\n')
        print('Case #' + str(case_num) + ': Bad magician!' + '\n')
    elif(flag == -1):
        f2.write('Case #' + str(case_num) + ': Volunteer cheated!' + '\n')
        print('Case #' + str(case_num) + ': Volunteer cheated!' + '\n')

    case_num = case_num + 1

f2.close()



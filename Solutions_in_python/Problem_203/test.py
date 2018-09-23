import numpy as np
file_x =  open('A-sample.in', 'r').readlines()
t = int(file_x[0])
output_file = open('cakes.txt', 'a')

def cakes(initial_list, rc_list):

    for i in range(rc_list[0]):
        last_var = 0
        for j in range(rc_list[1]):
            if initials_list[i][j] != 63:
                last_var = initials_list[i][j]
            if initials_list[i][j] == 63:
                initials_list[i][j] = last_var

    for i in range(rc_list[0] - 1, -1, -1):
        last_var = 0
        for j in range(rc_list[1]-1, -1, -1):
            if initials_list[i][j] != 0:
                last_var = initials_list[i][j]
            if initials_list[i][j] == 0:
                initials_list[i][j] = last_var

    for i in range(rc_list[0]):
        for j in range(rc_list[1]):
            if initials_list[i][j] == 0:
                print(initials_list, i, j)
                try:
                    if initials_list[i+1][j] == 0:
                        z = 1 / 0
                    for j in range(rc_list[1]):
                        initials_list[i][j] = initials_list[i+1][j]
                except Exception as e:
                    if initials_list[i - 1][j] == 0:
                        z = 1 / 0
                    for j in range(rc_list[1]):
                        initials_list[i][j] = initials_list[i-1][j]







file_index = 1

for i in range(1, t + 1):
    print("Case #"+str(i)+":")
    output_file.write("Case #{}:\n".format(i))
    rc_var = file_x[file_index]
    rc_list = [0, 0]
    initials_list = [[]]
    file_index += 1

    # print(rc_var)

    rc_list[0], rc_list[1] = [int(s) for s in rc_var.split(" ")]

    # print(rc_list)

    for z in range((rc_list[0])):
        list_var = []
        list_var2 = (file_x[file_index])
        file_index += 1

        for c in list_var2:
            list_var.append(ord(c))


        if (z < (rc_list[0] - 1)) | (i < t):
            initials_list.append(list_var[:-1])
        else:
            initials_list.append(list_var)

    initials_list = (initials_list[1:])
    np.array(initials_list)

    # print(initials_list)
    cakes(initials_list, rc_list)
    cakes(initials_list, rc_list)
    cakes(initials_list, rc_list)
    cakes(initials_list, rc_list)
    for i in range(rc_list[0]):
        strx = ""
        for j in range(rc_list[1]):
            strx = strx + (chr(initials_list[i][j]))
        print(strx)
        output_file.write("{}\n".format(strx))
    # print(initials_list)



output_file.close()
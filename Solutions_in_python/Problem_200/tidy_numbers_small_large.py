# t = int(input())  # read a line with a single integer
# """ Use this for running a .in file on your pc.
file_x =  open('B-large.in', 'r').readlines()
t = int(file_x[0])
# """
output_file = open('tidy_numbers2.txt', 'a')

def tidy_numbers(n):

    # print(n)
    strk = str(n)
    strx = []

    for i in strk:
        strx.append(int(i))

    length_var = len(strx) - 1

    for k in range(length_var, - 1, -1):
        if k == 0:
            # print(strx, len(strx))
            return strx

        else:
            if (strx[k]) < (strx[k - 1]):
                for j in range(k, length_var + 1):
                    strx[j] = 9

                strx[k - 1] = strx[k - 1] - 1



for i in range(1, t + 1):
    # s, m = [int(s) for s in input().split(" ")]
    n = int(file_x[i])
    y = tidy_numbers(n)
    y2 = ""

    if y[0] != 0:
        y2 = y2 + str(y[0])
    for z in range(1, len(y)):
        y2 = y2 + str(y[z])

    # print("Case #{}: {}".format(i, y2))
    output_file.write("Case #{}: {}\n".format(i, y2))

output_file.close()
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n = int(fin.readline())
for j in range(1, n + 1):
    ans_1 = int(fin.readline())
    matrix_1 = []
    for i in range(4):
        matrix_1.append(list(map(int, fin.readline().split())))
    ans_2 = int(fin.readline())
    matrix_2 = []
    for i in range(4):
        matrix_2.append(list(map(int, fin.readline().split())))
    res = []
    for i in range(1, 17):
        if i in matrix_1[ans_1 - 1] and i in matrix_2[ans_2 - 1]:
            res.append(i)
    if len(res) == 0:
        print('Case #' + str(j) + ':', 'Volunteer cheated!', file = fout)
    elif len(res) > 1:
        print('Case #' + str(j) + ':', 'Bad magician!', file = fout)
    else:
        print('Case #' + str(j) + ':', res[0], file = fout)
fin.close()
fout.close()
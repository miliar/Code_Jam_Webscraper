f = open('A-small-attempt0.in', 'r')
outf = open('output1.txt', 'w')
tot_row = 4

T = int(f.readline())

for test_ind in range(T):
    first_row_ind = int(f.readline())
    for i in range(tot_row):
        tmp = f.readline()
        if i + 1 == first_row_ind:
            first_row = set(map(int, tmp.split()))
    second_row_ind = int(f.readline())
    for i in range(tot_row):
        tmp = f.readline()
        if i + 1 == second_row_ind:
            second_row = set(map(int, tmp.split()))

    res = first_row.intersection(second_row)
    n_common = len(res)
    if n_common == 1:
        out_str = 'Case #' + str(test_ind + 1) + ': ' + str(res.pop()) + '\n'
    elif n_common > 1:
        out_str = 'Case #' + str(test_ind + 1) + ': Bad magician!\n'
    else:
        out_str = 'Case #' + str(test_ind + 1) + ': Volunteer cheated!\n'
    outf.write(out_str)

f.close()
outf.close()
        
    

    


fin = open ('c:/users/hai/my projects/google code jam/2011/qualification/A/A-large.in')
fout = open ('c:/users/hai/my projects/google code jam/2011/qualification/A/A-large.out','w')

T = int(fin.readline())

for testcase in range(1,T+1):
    
    l = fin.readline().split()
    N= int(l[0])
    l = l[1:]
    buttons = []
    for i in range(N):
        buttons.append((l[0],int(l[1])))
        del l[:2]

    pos_o = 1
    pos_b = 1
    time_o = 0
    time_b = 0

    min_times = []
    for btn in buttons:
        if btn[0] == 'B':
            time_b += abs(pos_b-btn[1])+1
            min_times.append(['B', time_b])
            pos_b = btn[1]
        if btn[0] == 'O':
            time_o += abs(pos_o-btn[1])+1
            min_times.append(['O', time_o])
            pos_o = btn[1]


    for i in range(1,len(min_times)):
        if min_times[i][1] <= min_times[i-1][1]:
            if min_times[i][0] == 'O':
                delay_o = min_times[i-1][1] - min_times[i][1] + 1
                for j in range(i, len(min_times)):
                    if min_times[j][0] == 'O':
                        min_times[j][1] += delay_o
            elif min_times[i][0] == 'B':
                delay_b = min_times[i-1][1] - min_times[i][1] + 1
                for j in range(i, len(min_times)):
                    if min_times[j][0] == 'B':
                        min_times[j][1] += delay_b
            else:
                assert ValueError

    all_time_o = max([0] + [x[1] for x in min_times if x[0] == 'O'])
    all_time_b = max([0] + [x[1] for x in min_times if x[0] == 'B'])
    all_time = max([all_time_o, all_time_b])


    outputline = 'Case #' + str(testcase)+': ' + str(all_time)
    fout.write (outputline+ '\n')
    
    


fin.close()
fout.close()

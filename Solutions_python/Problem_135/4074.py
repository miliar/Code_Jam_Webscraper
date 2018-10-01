f = open('A-small-attempt0.in','r')
fout = open('out1.txt','w')

numIter = int(f.readline())

for i in range(0,numIter):
    count = 0
    last_num = 0
    row1 = int(f.readline())
    first_cand = []
    second_cand = []
    for j in range(1,5):
        current_line = f.readline()
        if(j == row1):
            first_cand = current_line.split()

    row2 = int(f.readline())

    for j in range(1,5):
        current_line = f.readline()
        if(j == row2):
            second_cand = current_line.split()
            for element in second_cand:
                if(element in first_cand):
                    count += 1
                    last_num = element

    fout.write('Case #'+str(i+1)+': ')
    if(count == 0):
        fout.write('Volunteer cheated!\n')
    elif(count == 1):
        fout.write(last_num+'\n')
    else:
        fout.write('Bad magician!\n')
    

f.close()
fout.close()

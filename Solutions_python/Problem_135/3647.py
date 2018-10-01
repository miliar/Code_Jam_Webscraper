

def problem1(inputfile):
    f = open(inputfile,'r')
    lines = f.read().splitlines()
    f.close
    number_examples = int(lines[0])
    o = open("output.txt",'w')
    for i in range(number_examples):
        number = 0
        case = 0
        row_chosen1 = int(lines[(i*10) + 1])
        row1 = lines[(i*10) + row_chosen1 + 1]
        row1 = str(row1).split(' ')
        row_chosen2 = int(lines[(i*10) + 6])
        row2 = lines[(i*10) + row_chosen2 + 6]
        row2 = str(row2).split(' ')
        for g in range(len(row1)):
            for h in range(len(row2)):
                if int(row1[g]) == int(row2[h]):
                    if number == 0:
                        number = int(row1[g])
                        case = 1
                    else:
                        case = 2
        if number == 0:
            case = 3
        o.write("Case #")
        o.write(str(i+1))
        o.write(': ')
        if case == 1:
            o.write(str(number))
            o.write('\n')
        if case == 2:
            o.write("Bad magician!\n")
        if case == 3:
            o.write("Volunteer cheated!\n")
    o.close
    return;

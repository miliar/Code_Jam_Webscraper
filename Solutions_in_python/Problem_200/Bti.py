
fin = open('G:\B-small-attempt0.in','r')
fout = open('G:\B-small-attempt0.out','w')

count = -1
printl = 0
for line in fin:
    count += 1
    if count == 0:
        continue
    str1 = line.strip()
    str_list = list(str1)
    str_int = int(line)
    flag = 0
    while flag ==0:
        if len(str_list) == 1:
            flag = 1
            break
        for i in range(len(str_list)):
            later = i+1
            if later >= len(str_list):
                flag = 1
                break
            if int(str_list[i]) > int(str_list[later]):
                if i == 0 or int(str_list[later]) == 0:
                    str_int -= 1
                else:
                    for j in range(i+1,len(str_list)):
                        str_list[j] = '0'
                    str1 = "".join(str_list)
                    str_int = int(str1)
                str_list = []
                str1 = str(str_int)
                str_list = list(str1)
                break
    if flag == 1:
        if printl != 0:
            fout.write("\n")
        printl += 1
        fout.write("Case #%d: %d" %(count, str_int))
fin.close()
fout.close()
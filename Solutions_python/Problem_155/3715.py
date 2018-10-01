fin = open("A-small-attempt2.in","r")
fout = open("output1.txt", "w")
case = int(fin.readline())
for ic in range(case):
    data = fin.readline().split()
    total_stand = 0
    total_invite = 0
    for i, init in enumerate(data[1]):
        if total_stand < i and int(init) > 0:
            total_invite += i - total_stand
            total_stand += total_invite
        total_stand += int(init)
    fout.write("Case #{0}: {1}\n".format(ic+1, total_invite))
fin.close()
fout.close()    


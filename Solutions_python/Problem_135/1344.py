f = open("input2.in", "r")
fout = open("output.out", "w")
tot = f.readlines()

T = int(tot[0]) # numero di casi

indexstart = 1
indexstop = 11
i = 0
for x in range(T):
    i+=1
    shit = tot[indexstart:indexstop]
    #print shit
    indexstart=indexstop
    indexstop=indexstop+10
    firstrow=int(shit[0])
    secondrow=int(shit[5])
    firstset = shit[1:5]
    secondset= shit[6:10]

    firstlist = []
    secondlist = []
    for x in firstset:
        firstlist.append(x.strip().split(" ")) # e ora ho liste di liste

    for x in secondset:
        secondlist.append(x.strip().split(" ")) # e ora ho liste di liste

    #print firstlist
    #print secondlist

    numbers1 = firstlist[firstrow-1]
    numbers2 = secondlist[secondrow-1]
    print numbers1
    print numbers2
    
    result = []
    for x in numbers1:
        for y in numbers2:
            if x==y:
                result.append(x)

    print result
    
    if len(result) == 1:
        fout.write("Case #{0}: {1}\n".format(i,result[0]))
    elif len(result) > 1:
        fout.write("Case #{0}: Bad magician!\n".format(i))
    else:
        fout.write("Case #{0}: Volunteer cheated!\n".format(i))


f.close()
fout.close()

from math import ceil, sqrt
infile = open("infile.txt","r")
inlist = infile.readlines()
outfile = open("out.txt","w")
cases = eval(inlist.pop(0))
for i in range(len(inlist)): inlist[i] = inlist[i].strip("\n")

table = []
for i in range(len(inlist)): table.append([eval(val) for val in inlist[i].split()])

for case in range(len(table)):
    [start,end] = table[case]
    [a,b] = [int(ceil(sqrt(start))), int(math.sqrt(end))]
    count = 0

    for i in range(a,b+1):
        if str(i)==str(i)[::-1]:
            j = i**2
            if str(j)==str(j)[::-1]: count+=1

    print("Case #"+str(case+1)+":",count, file=outfile)


outfile.close()
infile.close()
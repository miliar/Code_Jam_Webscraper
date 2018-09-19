fin = open('A-small-attempt0.in')
fout = open('output.out', 'w')

def magicianGuess(table1, ans1, table2, ans2):
    s1=set()
    s2=set()
    for e1 in table1[ans1-1]:
        s1.add(e1)
    for e2 in table2[ans2-1]:
        s2.add(e2)
    i = s1.intersection(s2)
    if len(i)==0:
        return "Volunteer cheated!"
    elif len(i)>1:
        return "Bad magician!"
    else:
        for e in i:
            return e


lineNb=0
for line in fin:
    if lineNb==0:
        lineNb+=1
        continue
    if lineNb%10==1:
        ans1 = int(line.strip())
        table1=[]
    if lineNb%10>=2 and lineNb%10<=5:
        row=[]
        for el in line.strip().split(" "):
            row.append(int(el))
        table1.append(row)
    if lineNb%10==6:
        ans2 = int(line.strip())
        table2=[]
    if lineNb%10==0 or (lineNb%10>=7 and lineNb%10<=9):
        row = []
        for el in line.strip().split(" "):
            row.append(int(el))
        table2.append(row)
        if lineNb%10==0:
            fout.write("Case #"+str(lineNb//10)+": "+str(magicianGuess(table1, ans1, table2, ans2))+"\n")
    lineNb+=1
fout.close()

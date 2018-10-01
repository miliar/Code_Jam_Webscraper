f = open("A-large.in","r")
#f = open("A-large-practice.in","r")
g = open("test.txt","w")

cases = int(f.readline())
caseno = 1

for m in range(cases):
    g.write("Case #" + str(caseno) + ": ")

    line = str(f.readline())
    shyLevel = int(line.split(" ")[0])
    people = str(line.split(" ")[1])
    l = list(str(people))

    count = 0
    add = 0
    total = int(0)
    totaladd = 0
    #g.write(str(l))

    for n in range(shyLevel+1):
        if(total<count):
            add = add+1
        total = total + int(l[count])+add
        count = count+1
        totaladd = totaladd+add
        add=0

    #g.write(str(total))
    g.write(str(totaladd) + "\n")
    caseno = caseno+1

f.close()
g.close()




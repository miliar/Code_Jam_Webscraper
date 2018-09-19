infile=open('D-large.in','r')
lines=infile.readlines()
infile.close()
outfile=open('ans4.txt','w')
test=int(lines[0])
for i in range(test):
    text = "Case #" + str(i+1) + ": "
    cases = lines[1+(i*3):4+(i*4)]
    naomi = sorted(cases[1].strip().split(" "))
    ken = sorted(cases[2].strip().split(" "))
    #war
    war = 0
    for j in range(len(naomi)):
        if naomi[-(j+1)] > ken[-1]:
            war += 1
        else:
            ken.pop()
    #deceit
    naomi = sorted(cases[1].strip().split(" "))
    ken = sorted(cases[2].strip().split(" "))
    deceit = 0
    foo=0
    for j in range(len(naomi)):
        if naomi[j]<ken[foo]:
            ken.pop()
        else:
            deceit += 1
            foo += 1 
    outfile.write(text)
    outfile.write(str(deceit))
    outfile.write(" ")
    outfile.write(str(war))
    outfile.write("\n")
outfile.close()

print("done")

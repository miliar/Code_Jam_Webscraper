#Google Code Jam Problem 1
#Andrew Penland
#April 13, 2012

inputlines = []
inputlines.append("ejp mysljylc kd kxveddknmc re jsicpdrysi")
inputlines.append("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
inputlines.append("de kr kd eoya kw aej tysr re ujdr lkgc jv")

outputlines = []
outputlines.append("our language is impossible to understand")
outputlines.append("there are twenty six factorial possibilities")
outputlines.append("so it is okay if you want to just give up")

Googlerese = {'y':'a', 'e':'o', 'q':'z'}

for i in range(len(inputlines)):
    thestring = inputlines[i]
    otherstring = outputlines[i]
    for x in range(len(thestring)):
        if not(Googlerese.has_key(thestring[x])):
            Googlerese[thestring[x]] = otherstring[x]

Googlerese['z'] = 'q'

f1 = open('C:/A-small-attempt2.in','r')
f2 = open('C:/A-small-attemptanswer.txt','w')

numlines = f1.readline()
lines = f1.readlines()

for i in range(int(numlines)):
    myline = lines[i]
    mystring = "Case #" + str(i + 1) + ": "
    for i in range(len(myline)):
        if myline[i] == "\n":
            f2.write(mystring + "\n")
        else:
            mystring = mystring + Googlerese[myline[i]]


f2.close()
        
        

          
            
        

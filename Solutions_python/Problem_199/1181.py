def outp(a,b):
    file=open("output.txt","a")
    s="Case #"+str(a+1)+": "+str(b)+"\n"
    file.write(s)
    file.close
    print(s)

q=open ("output.txt","w")
q.close()
inp = open("A-large.in","r")
a= []
for line in inp:
    if "\n" in line:
        a.append(line[0:-1])
    else:
        a.append(line)
inp.close()
inpNum =int(a.pop(0))
for ii in range(inpNum):
    qn = a[ii].split(" ")
    leng = int(qn[1])
    setup = list(qn[0])
    setLen = len(setup)
    count = 0
    for i in range(setLen):
        if setup[i] == "-":
            if i+leng > setLen:
                count = "IMPOSSIBLE"
                break
            count += 1
            for p in range(leng):
                pan = p+i
                if setup[pan] == "-":
                    setup[pan] = "+"
                else:
                    setup[pan] = "-"
    outp(ii, count)
            
    
    
    

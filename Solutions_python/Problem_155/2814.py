fin=open("A-large.in","r")
fout=open("output.txt","w")

cases=int(fin.readline())

for case in xrange(cases):
    line = fin.readline()
    c = line.split(" ")[0]
    sall = line.split(" ")[1]
    
    clapped = 0
    requiredClappers = 0
    for i in xrange(int(c) + 1):
        s = int(sall[i])
        if i > clapped:
            requiredClappers += i - clapped
            clapped += i - clapped
        clapped += int(s)
        i = i + 1
        
    fout.write("Case #{0}: {1}\n".format(str(case + 1) , requiredClappers))
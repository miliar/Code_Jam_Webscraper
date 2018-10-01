fin = open('A-large.in','r')
fout = open('x.in','w')
T = int(fin.readline())
count =1
while count <= T :
    line = fin.readline()
    line = line.rstrip()
    words = line.split()
    max_shy = int(words[0])
    aud = words[1]
    need = 0
    c1 = 1
    '''if (int(aud[0]) > max_shy) :
        str1 = "Case #" + str(count) + ": " + str(0) + "\n"
        fout.write(str1)
        count = count+1
        continue
    else :'''
    while (c1 <= max_shy) :
        if int(aud[c1])!=0 :
            total = 0
            c2 = 0
            while c2 < c1 :
                total = total + int(aud[c2])
                c2 = c2 + 1
            if need+total < c1 :
                    need = need + (c1-(total+need))
        c1 = c1 + 1
    str1 = "Case #" + str(count) + ": " + str(need) + "\n"
    fout.write(str1)
    count = count+1
fin.close()
fout.close()

        

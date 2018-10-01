
#input file
#f = open("A-small-attempt0.in.txt","r")
f = open("A-large.in.txt","r")

line = f.readline()
setnum = int(line)

for i in range(1,setnum+1):
    line = f.readline()
    inp = line.split(" ")
    m = int(inp[0])
    audience = str(inp[1])[0:-1]
    ans = 0

    #print (m,audience)

    for j in range(m+1):
        #print ("audience="+audience)
        check = 0
        if (j==0):
            continue
        for k in range(j):
            check += int(audience[k])
        if (check >= j):
            continue
        else:
            ans += 1
            if (j>=2):
                audience=audience[0:j-1]+'1'+audience[j:len(audience)]
            else:
                audience='1'+audience[j:len(audience)]



    #write output
    print ("Case #%d: %d" % (i, ans))

f.close()

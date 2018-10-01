fin = open("C-large.in")
fout = open("q3.output.txt", "wt")
testCnt = int(fin.readline())

for i in range(0, testCnt):
    itemCnt = int(fin.readline())
    strItems = fin.readline().strip()
    items = map(int, strItems.split(" "))
    items.sort()
    #print itemCnt
    #print items

    fout.write("Case #%d: " % (i+1)) 
    xorval = 0
    sumAll = 0
    for num in items:
        xorval = xorval ^ num
        sumAll = sumAll + num
        
    if xorval!=0:
        fout.write("NO\n")
    else:
        fout.write("%d\n" % (sumAll-items[0]))

print "OK"
fin.close()    
fout.close()

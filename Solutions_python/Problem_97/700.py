fin = open("C-large.in","r")
fout = open("C-large.out","w")

TestCases = int(fin.readline())
for x in xrange(TestCases):
    string = "Case #"+ str(x+1) + ": "
    print "Case #", str(x),": "
    count = 0
    row = fin.readline().split(" ")
    A = int(row[0])
    B = int(row[1])
    for num in xrange(A,B):
        tmp_list = []
        str_num = str(num)
        s = str_num
        for ch in xrange(len(str_num)):
            s = s[len(s)-1:]+ s[:len(s)-1]
            if s in tmp_list:
                continue
            tmp_list.append(s)
            #print s
            if s > str_num and s< row[1]:
                count += 1
    string += str(count) + "\n"
    print count
    fout.write(string)
fout.close()
            
        
    
    
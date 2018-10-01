##Codejam question one


with open('A-large.in', 'r') as fin:
    with open('file.out', 'w') as fout:
        lnCount = 0
        T = 1001
        for line in fin:
            tokens = line.split()
            if(lnCount == 0):
                T = int(tokens[0].strip())
    ##            print "T: "+ str(T)
            else:
                inLine = [str(token.strip()) for token in line.split()]
                sMax = int(inLine[0])
    ##            print "sMax: "+str(inLine[0])
                people =  map(int, list(inLine[1]))
    ##            print inLine[1]
    ##            print "people: "+str(people[0:])
                total = 0
                i = 0
                needed = 0
                for peeps in people:
    ##                print "Top\tTotal: "+str(total)+", i: "+str(i)+", needed: "+str(needed)
                    if(total+needed<i):
                        needed += i-(total+needed)
    ##                    print i-total
                    total += peeps
                    if(total+needed >= sMax):
    ##                    print "breaking!"
    ##                    print "Bottom\tTotal: "+str(total)+", i: "+str(i)+", needed: "+str(needed)
                        break
    ##                print "Bottom\tTotal: "+str(total)+", i: "+str(i)+", needed: "+str(needed)
                    i +=1
                fout.write("Case #"+str(lnCount )+": "+str(needed)+"\n")
    ##        nums = [int(token.strip()) for token in line.split()]
            lnCount = lnCount +1;

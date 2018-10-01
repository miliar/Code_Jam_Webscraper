
def feed( garbled, plain, mydict ):
    if len(garbled) != len(plain):
        print "Problema con largos de strings"

    for i in range(len(garbled)):
        mydict[garbled[i]] = plain[i]


def show( dict ):
    for i in thedict:
        print i, thedict[i]

    print ""
    print len(thedict), thedict

def transform( t, thedict ):
    s = ""
    for i in range(len(t)):
        if t[i] not in thedict:
            # print
            # print t[i], " was not in the dictionary before"
            notfound = []
            for j in range(26):
                target = chr(ord("a")+j)
                found = False
                for k in thedict:
                    if thedict[k] == target:
                        found = True
                #         print k, " -> ", target

                if found == False:
                #     print "No encontre ", target
                    notfound.append( target )
            # print
            thedict[t[i]] = notfound.pop() 
            # print " adding ", t[i], " -> ", thedict[t[i]]
            # if len(notfound) > 0:
            #     print "Still to consider :", notfound

        s = s + thedict[t[i]]
    return s
        
thedict = {}
feed( "yqe", "azo", thedict )

feed( "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand", thedict )
feed( "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities", thedict )
feed( "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up", thedict )

# show( thedict )

n = int( input() )

# print n
for i in range(n):
    line = raw_input()
    t = transform( line, thedict )
    print "Case #"+str(i+1) + ":", t
    l1 = len(line)
    l2 = len(t)
    # print l1,line
    # print l2, t
    # if l1 != l2:
    #     print "*********** HERE HERE HERE **************"
    # print "----------------------------------------------"

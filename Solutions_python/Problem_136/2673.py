def CCA(inputfile, outputfile):
    print "bezig"
    inputdata = open(inputfile, "r")
    outputdata = open(outputfile, "w")
    T = int(inputdata.readline())
    for case in range(T):
        C,F,X = map(float,inputdata.readline().split())
        VorigTijd = CalculateTime(0,C,F,X)[0]
        HuidgTijd, TijdVoorFarms = CalculateTime(1,C,F,X)
        i = 2
        #print C,F,X
        #print VorigTijd,HuidgTijd
        while HuidgTijd < VorigTijd:
            VorigTijd = HuidgTijd
            HuidgTijd, TijdVoorFarms =  CalculateTimeFaster(i,C,F,X,TijdVoorFarms)
            i+=1
            #print VorigTijd,HuidgTijd,i
        #print
        outputdata.write("Case #" + str(case+1) + ": " + str("%.7f" % VorigTijd) + "\n")
    inputdata.close()
    outputdata.close()
    print "done"

def CalculateTime(farms,C,F,X):
    #print "calctime----------------\ncalctime: ",farms
    optelling = 0
    for i in range(farms):
        optelling += C/(2+(i*F))
        #print "calctimef: ",optelling, C/(2+(i*F))
    TijdVoorFarms = optelling
    optelling += X/(2+(farms*F))
    #print "calctimex: ",optelling, X/(2+(farms*F))
    return optelling,TijdVoorFarms
    
def CalculateTimeFaster(farms,C,F,X,ReedsBerekend):
    #print "tijdbespaard"
    TijdVoorFarms = ReedsBerekend + C/(2+((farms-1)*F))
    optelling = TijdVoorFarms + X/(2+(farms*F))
    return optelling, TijdVoorFarms

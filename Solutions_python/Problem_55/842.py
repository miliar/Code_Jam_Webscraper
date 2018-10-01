import re
filename = 'C-small-attempt0'
infilename = filename+'.in'
outfilename = filename+'.out'
infile = open(infilename,'r')
outfile = open(outfilename,'w')
ntestcases = infile.readline().rstrip()
print "Solving", ntestcases, "test cases.\n"
i=0
results=[]
def solve(i, r, k, n, g=[]):
    if n==1:
        nf = "1 group."
    else:
        nf = str(n)+" groups."
    print "Solving test case #"+str(i), "with", str(r), "rides,", k, "capacity, and", nf
    print "   Group(s):", g,"\n"
    if sum(g)<=k:
        totalincome = sum(g)*r
        print "   Easy way found. Because the total number of riders is less than or equal to the capacity of a single ride, I deduce that", sum(g), "total riders riding", r, "times brings in", totalincome, "euros.\n"
        return totalincome
    ridenum = 0
    totalincome = 0
    while ridenum < r:
        rideincome = 0
        remainingspots = k
#        print "   Ride", ridenum+1, "of", r
#        print "      Before the ride, the queue looks like:", g
        ride=[]
        while True:
            if g[0] <= remainingspots:
                remainingspots = remainingspots - g[0]
#                print "      Group of", g[0], "fits, leaving", remainingspots, "spots available."
                rideincome = rideincome+g[0]
                ride.append(g.pop(0))
#                print "      Current state of queue:",g
            else:
#                print "      Group of",g[0],"does not fit. Starting ride... returning riders to queue."
#                print "      Returning riders to queue:"
                a = 0
                lenride=len(ride)
                while a < lenride:
#                    print "         Taking group of", ride[0], "and putting into queue."
                    g.append(ride.pop(0))
                    a = a+1
#                    print "         Ride looks like:", ride
#                    print "         Queue looks like:", g
                        
#                print "      After the ride, the queue looks like:", g
                break

#        print "      That ride made",rideincome,"euros."
        totalincome=totalincome+rideincome
        ridenum=ridenum+1
    print "   Total income of test case", str(i)+":", totalincome, "euros\n"
    return totalincome

while i<int(ntestcases):
    firstline=infile.readline()
    secondline=infile.readline()
    firstline = firstline.rstrip()
    secondline = secondline.rstrip()
    parsedfirstline = re.split(":? ", firstline, 3)
    secondline = re.split(":? ", secondline, 1000)
    parsedsecondline=[]
    for gi in secondline:
        parsedsecondline.append(int(gi))
    results.append(solve(i+1, int(parsedfirstline[0]),int(parsedfirstline[1]),int(parsedfirstline[2]),parsedsecondline))
    i=i+1
    
formattedresults = ""
for casenum in range(0,int(ntestcases)):
    formattedresults = formattedresults + "Case #" + str(casenum+1) + ": " + str(results[casenum]) + "\n"

print "\n  Results:"
print formattedresults
print "Writing results to", outfilename
print outfile
outfile.write(formattedresults)
print "Done."
outfile.close()
infile.close()

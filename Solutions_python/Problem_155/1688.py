#https://code.google.com/codejam/contest/6224486/dashboard

flenames = ["test","A-small-attempt0","A-large"]  #.in for input .out for output
flemask = [0,0,1]   #toggle whether to run (1) or dont run (0) the filenames

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

            inp = flein.readline().split()
            maxS = int(inp[0])
            pplstr = inp[1]
            ppl = []
            for pplctr in range(maxS+1):
                ppl.append(int(inp[1][pplctr]))

#            print maxS, ppl

            newppl = 0
            totnewppl = 0
            totalppl = 0

            for ctr in range(maxS+1):
                totalppl = totalppl + ppl[ctr] + newppl
                newppl = max(0,ctr + 1 - totalppl)
                totnewppl += newppl

            outpA = totnewppl

            outstr = "Case #{}: {}".format(ctrL+1,outpA)
            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()


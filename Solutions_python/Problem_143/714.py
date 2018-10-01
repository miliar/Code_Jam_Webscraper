flenames = ["test","B-small-attempt0","B-large-practice"]  #.in for input .out for output
flemask = [1,1,0]   #toggle whether to run (1) or dont run (0) the filenames

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\downloads\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\downloads\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):
            inA, inB, inK = [int(inp) for inp in flein.readline().split()]

            lesser = min(inA,inB)
            bigger = max(inA,inB)

            countwin = 0
            for ctr1 in range(0,inA):
                for ctr2 in range(0,inB):
                    comb = ctr1 & ctr2
                    if comb < inK:
                        countwin += 1


            outp = countwin

            outstr = "Case #{}: {}".format(ctrL+1,outp)
            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()


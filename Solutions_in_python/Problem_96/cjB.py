filename = "B-large"
infile = open("{}.in".format(filename))
outfile = open("{}.out".format(filename), 'w')


T = int(infile.readline())
for t in range(1,T+1):
    print "\n\nCase {}".format(t)
    params = infile.readline().strip().split(' ')
    N, S, p = [int(x) for x in params[:3]]
    scores = [int (x) for x in params[3:]]

    count = 0
    for score in scores:
        s = score / 3
        print "s is {}".format(s)
        if score != 0:
            if score % 3 == 0:
                print "mod = 0"
                if s+1 == p and S > 0:
                    print "spending a suprise"
                    S -= 1
                    s += 1
            if score % 3 == 1:
                print "mod = 1"
                s += 1
            if score % 3 == 2:
                print "mod = 2"
                s += 1
                if s+1 == p and S > 0:
                    print "spending a suprise"
                    S -= 1
                    s += 1
        if s >= p:
            print "adding a googler"
            count += 1

    outfile.write("Case #{}: {}\n".format(t, count))

infile.close()
outfile.close()

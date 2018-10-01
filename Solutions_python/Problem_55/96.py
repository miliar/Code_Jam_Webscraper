def solve(filecontent):
    lines = filecontent.splitlines()
    T = int(lines[0])
    out = []
    for tcase in xrange(1,T+1):
        line1 = lines[2*tcase - 1].split(" ")
        line2 = lines[2*tcase - 0].split(" ")
        R = int(line1[0])
        k = int(line1[1])
        N = int(line1[2])
        
        g = map(int,line2)
        quick = {}
        for start in xrange(N):
            seatsFilled = 0
            i = 0
            while seatsFilled + g[(start+i) % N] <= k and i < N:
                seatsFilled += g[(start+i) % N]
                i += 1
            quick[start] = ((start+i) % N, seatsFilled)

        earnings = 0
        queueHead = 0
        while R > 0:
            if R % 2 == 1:
                queueHead, thisEarnings = quick[queueHead]
                earnings += thisEarnings
            # advance quick from N steps to 2*N steps
            quick2 = {}
            for start in xrange(N):
                head1, earn1 = quick[start]
                head2, earn2 = quick[head1]
                quick2[start] = (head2, earn1+earn2)
            quick = quick2
            # reduce R to next step
            R = R / 2
            

        tcaseOut = ("Case #%d: " % (tcase,))
        tcaseOut += "%d" % (earnings)
        out.append(tcaseOut)
    return "\n".join(out)

f = file("codejam/C-large.in").read()
file("codejam/C-large.out",'w').write(solve(f))

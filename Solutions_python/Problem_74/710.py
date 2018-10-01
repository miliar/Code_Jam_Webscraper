f = open("input_A.txt","r")
f2 = open("output_A.txt","w")
f.readline()

def solve(os,bs):

    #print "o : " ,os, " ,  b : " ,bs
    on , bn = len(os), len(bs)
    oi, bi = 0,0
    time = 0
    while (oi < on and bi < bn ):
        #print oi, bi, time
        #smaller
        def check( o1, o2):
            d1 = 0
            time = 0
            if o1[0] < o2[0]:
                time = o1[1] + 1
                o1[1] = 0
                d1 = 1
                o2[1] = max( 0 , o2[1] - time)
            return o1, o2, d1, time

        os [oi], bs[bi], objD, timeD = check(os [oi], bs[bi])
        time += timeD
        oi+=objD
        if objD == 1: 
            continue
        bs[bi], os [oi], objD, timeD = check(bs[bi], os [oi])
        bi+=objD
        time += timeD
        if objD == 1: 
            continue


    #print oi, bi, time
         
    time += sum( map(lambda x: x[1]+1,os[oi:])) + sum( map(lambda x: x[1]+1,bs[bi:]))
    #print "o : " ,os, " ,  b : " ,bs,"\n"

    return time

idx = 0
for l in f:
    numbers = l.strip().split()[1:]
    #print l
    pairs = [ (numbers[i],int(numbers[i+1])) for i in range(0,len(numbers),2) ]
    os , bs = [] , []
    po, bo = 1, 1
    for i, pair in enumerate(pairs):
        if pair[0] == "O":
            os.append([i,abs(po - pair[1])])
            po = pair[1]
        elif pair[0] == "B":
            bs.append([i,abs(bo - pair[1])])
            bo = pair[1]            

    time = solve(os,bs)
    idx += 1
    f2.write( "Case #%d: %d\n" % (idx,time) )

f2.close()

f.close()

TXT=open('bin.txt')
inputlist=TXT.readlines()
TXT.close()

testCases=int(inputlist[0].strip())

line_cnt=1
OUT=open("bout.txt",'w')
for tc in xrange(1,testCases+1):
    thisList=inputlist [line_cnt ].strip().split(' ')
    line_cnt+=1
    C=float(thisList[0])
    F=float(thisList[1])
    X=float(thisList[2])
    nF=1
    time=0.0
    rate=2.0
    if X<C:
        time+=X/2.0
        OUT.write(  "Case #%d: %.7f\n" %(tc,time))
    else:
        #print tc
        cur_time=X/rate
        next_time=(C/rate)+(X/((nF)*F+2.0))
        time+=C/rate
        rate=nF*F+2.0
        nF+=1
        out_time=cur_time
        #print cur_time
        #print next_time
        while (cur_time>next_time):
            out_time=next_time
            cur_time=next_time
            time+=C/rate
            rate=nF*F+2.0
            next_time=time+(X/rate)
            #print cur_time
            #print next_time

            nF+=1
        OUT.write(  "Case #%d: %.7f\n" %(tc,out_time))

OUT.close()


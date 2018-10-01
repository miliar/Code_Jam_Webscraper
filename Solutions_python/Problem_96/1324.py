import os
inp = open('B-large.in', "r")
out = open('outputBL.out', "w")
text = inp.read()
x = text.split("\n")
count = int(x[0])
over_scores = []
for i in range (0, int(count)):
    c = i+1
    line = x[c].split(" ");
    g= line[0]
    s = int(line[1])
    p = int(line[2])
    scores = line[3:]
    can =0
   # print g, s, p
    for score in scores:
        k = p - (int(score)/3)
        m = int(score)%3
       # print "SCORE/3",int(score)/3, "SCORE", score,"k", k,"m", m
        if k<=0:
            can+=1
        #    print "CAN1"
        elif k==1:
            if m>0:
                can+=1
            #    print "CAN2"
            elif m==0 and s>0 and int(score)/3!=0:
                #print s
                s=s-1
                can+=1
               # print "CAN4"
              #  print "SUB"
                
        elif k==2 and m==2 and s>0:
           # print "CAN3 \n SUB"
            can+=1
            s = s-1
        
    out.write("Case #"+str(c)+": "+str(can)+"\n")
    
    #out.write()
out.close()
inp.close()


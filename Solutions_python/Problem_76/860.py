#fread=open('z.in','r')
fread=open('C-small-attempt1.in','r')
fwrite=open('out.txt','w')

total_cases=fread.readline().strip()
for i in range(int(total_cases)):
    numofcandies = int(fread.readline().strip())
    line1 = fread.readline().strip()
    l1= line1.split() 
    l2=[]
    for j in range(numofcandies):
        l2.append(int(l1[j]))
    #l2.sort()
    seans_pile_maxvalue=0
    n=0
    l2str=""
    while(n<numofcandies):
        temp1=l2[0]
        l2[0]=l2[n]
        l2[n]=temp1
        l2str=l2
        #print "l2str",l2str
        j=0
        x=0
        xi=0
        xstr=""
        while(j<numofcandies-1):
            xstr=xstr+" "+str(l2[j])
            x=x ^ l2[j]
            xi=xi + l2[j]
            k=j+1
            y=0
            yi=0
            ystr=""
            while(k<numofcandies):
                ystr=ystr +"  "+ str(l2[k])
                #print "before y,l2[k]:",y,",",l2[k]
                y=y ^ l2[k]
                #print "after: y",y
                yi=yi + l2[k]
                k=k+1
            #print "xstr=",xstr
            #print "ystr=",ystr
            if(x==y): #Acc to Patrik, both are equal.
                #print "Acc to Patrik, both are equal.:     x=",x,"   y=",y
                if (xi>=yi and seans_pile_maxvalue<=xi): 
                    seans_pile_maxvalue=xi
                elif(yi>=xi and seans_pile_maxvalue <= yi):
                    seans_pile_maxvalue=yi
            j=j+1
    
        n=n+1
    if (seans_pile_maxvalue == 0):
        o_string="Case #"+str(i+1)+": NO\n"
    else:
        o_string="Case #"+str(i+1)+": "+str(seans_pile_maxvalue)+"\n"
    #print o_string
    fwrite.write(o_string)
       

    
fread.close()
fwrite.close()

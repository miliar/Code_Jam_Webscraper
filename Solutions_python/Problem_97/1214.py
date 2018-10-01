def input():
    filename="C-small-attempt0.in"
    infile=open(filename,"r")
    num_cases=int(infile.readline())
    print num_cases,"cases"
    count=0
    cases=[]
    for line in infile:
        count+=1
        (num_A,num_B)=line.split()
        cases.append((int(num_A),int(num_B)))
        print "case#",count," ",num_A,num_B
    infile.close()
    if count != num_cases:
        print "error in number of cases"
    return (num_cases,cases)



def process((num_A,num_B)):
    start=num_A
    count=0
    pair=[]
    num_pos=1
    while(True):
        if (start / (10**num_pos)) == 0:
            #print "breaking at",num_pos
            break
        else:
            num_pos+=1
    base_num=10**(num_pos-1)
    print "base_num",base_num,"num_pos",num_pos
    while(start<=num_B):
        #print "start=",start
        n=start
        for i in range(1,num_pos):
            m=n%(10**i) * ( 10**(num_pos-i)) + n/(10**i)
            #m=base_num * (n%10) + n/(10**i)
            #print "n=",n," m=",m
            if num_A <=n and n<m and m<=num_B:
                if(n,m) not in pair:
                    pair.append((n,m))
                    count+=1
                    #print "adding","n=",n," m=",m
        start+=1
    return count
        

            
            
            

#main()
(num_cases,cases)=input()
outfilename="output.txt"
outfile=open(outfilename,"w")
count=0
for case in cases:
    print case
    result= process(case)
    count+=1
    outfile.write("Case #"+str(count)+": "+str(result)+"\n")
outfile.close()

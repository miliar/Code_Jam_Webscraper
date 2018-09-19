#python
#prima donna
#from decimal import *
infile="A-small-attempt0.in" #prima.in"#"B-large-practice.in"
#clears outfile.txt
outfileFlush=open("outfile.txt", "w")
outfileFlush.write("")
outfileFlush.close()


def writeout(answer,x):
#converts query from main loop (which is the answer list - ie place in list of items that add up to credit)
        answerTXT=""
        #print answer
        ##raw_input("in writeout")
        #if answer=="":
        #    return
        #for q in answer:
        #answerTXT=answerTXT+answ" "+q #might neeed str(q)
        answerTXT="Case #"+str(x+1)+": "+str(answer)+"\n"
        print answerTXT
        #writeout(answer)# sends a line to the output file (see def)


        outfile=open("outfile.txt", "a")
    #print "writewout",answer
        outfile.write(answerTXT)#DEBUG make sure this appends......
        outfile.close()#pass

def writeout2(answer,field,x):
#converts query from main loop (which is the answer list - ie place in list of items that add up to credit)
        answerTXT=""
        #print answer
        ##raw_input("in writeout")
        #if answer=="":
        #    return
        #for q in answer:
        #answerTXT=answerTXT+answ" "+q #might neeed str(q)
        answerTXT="Case #"+str(x+1)+": "+""+"\n"
        print answerTXT
        #writeout(answer)# sends a line to the output file (see def)
        

        outfile=open("outfile.txt", "a")
    #print "writewout",answer
        outfile.write(answerTXT)#DEBUG make sure this appends......
        for row in field:
          outfile.write(row+"\n")
        outfile.close()
        #pass


#cookie farm

#read in data
def readinp(infile):
    testshy={}
    testaud={}
    tests=0
    with open(infile,'r') as inputf:
        count=0
        for line in inputf:
            if count==0:
                value=line.split()
                tests=int(value[0])
                count=1
                continue
        
            value=line.split()
            #print value
            #print count
            #print tests
            testshy[count]=value[0]#line.strip()
            testaud[count]=value[1]
            count=count+1
          # print(count,value,testcases[0])
    return(testshy,testaud,tests)
#testcases=[]#copy from site
#for line in
#testcases.append

#shyness 
#logic
# need at least 1 at aud[0], then 
#add up shyness players
def needed(lst):
    l=len(lst)
    lstint=[]
    needs=0
    maxshy=l-1
    count=0
    for i in lst:#which is a string
        
        lstint.append(int(lst[count]))
        count=count+1
    tot=sum(lstint)
    print('lst',lst,lstint)
    print tot
    for b in lst:
        lstint.pop()
        if sum(lstint)>=len(lstint):
            #its ok
            continue
        else: 
            needs=needs+(len(lstint)-sum(lstint))
            lstint[0]=lstint[0]+needs#add the number to the begginng
    return(needs)       
        
        
    #is there astarter/
    if lst[0]=="0":
        needs=needs+1
    for j in lstint:
        pass#if j==

#start

tstshy,tstaud,tests=readinp(infile)
print tstaud
for a in range(tests):
    answer=needed(tstaud[a+1])
    writeout(answer,a)

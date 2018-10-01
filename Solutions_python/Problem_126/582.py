# standard functions
#File input
file2test="cons1as.in"
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
        answerTXT="Case #"+str(x)+": "+str(answer)+"\n"
        print answerTXT
        #writeout(answer)# sends a line to the output file (see def)


        outfile=open("outfile.txt", "a")
    #print "writewout",answer
        outfile.write(answerTXT)#DEBUG make sure this appends......
        outfile.close()#pass

def check(testn,n):
	vowels=['a','e','i','o','u']
	vowls=0
	leng=0
	print "testting ",testn
	for let in testn:
		if let in vowels:
			print testn,leng,let
			if leng>=n:return True
			vowls=vowls+1
			if len(testn)-vowls<n:return False
			leng=0
		else: 
			leng=leng+1
			#print "added one ", leng
			if leng>=n:return True
	print "must be less than ",n," ? ",leng
	return False
	if len(testn)-vowls>=n:
		return True
	if len(testn)-vowls<n:
		return False
	print "00000PS"
		
	

def readboard(cases):
	line=file2.readline().split()
	#print line
	a=0
	count=0
	n=int(line[1])
	name=line[0]
	print a, n, name, len(name)
	while a+n<=len(name):
		for b in range(len(name)-n+1):
			print "a+n_n",a+n+b
			if a+n+b>len(name):continue
			testn=name[a:a+n+b]
			#print testn
			if check(testn,n):
				print count
				count=count+1
		a=a+1
		print "a",a,"b",b,"n",n,
	print count
	return count
		
#main program loop
x=1 #?right place
cases=1
file2=open(file2test,"r")
no_cases=file2.readline().split()#dependent on structure as defined - this is just to ignore the first line for the purpose of this exercise
no_cases=int(str(no_cases[0]))
print(no_cases," numb of Cases pre-main while")
# now need to collect the next case
cases=1
while cases<=no_cases:
    #ncase=file2.readline().split()
    #blankline=file2.readline().split()
    #answer="UNKNOWN"
    ttb=readboard(cases)#case may not be needed
    #fred=checkcase(ncase)
#    ted=lookforwin(ttb)
 #   answer=format(ted)
    answer=ttb
    writeout(answer,cases)
    print cases,"case"
    cases=cases+1
file2.close()
print("Finished")


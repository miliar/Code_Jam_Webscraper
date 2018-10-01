#nbCases
#NGoog Surpr atLeastPAuMax TotalPourChaqGoogler

debug=0
fname="rec3.in"
file=open(fname)


out=open("out_"+fname, "w")


from pprint import pprint
nbCases=int(file.readline())
for j in range(1,nbCases+1):
	line=file.readline()
	line=line.split()
	if debug:
		pprint(line)
	a=int(line[0])
	b=int(line[1])
	compte=0
	
	for i in range(a,b):
		st=str(i)
		st2=st
		#print st+":"
		pair=[]
		for k in range(len(st)-1):
			st2=st2[1:]+st2[0]
			#print st2
			if int(st2)>int(st) and int(st2)<=b and int(st2[0])<>0:
				if st2 not in pair:
					#print "OK"
					#print st+"-"+st2
					compte=compte+1
					pair.append(st2)
				
				
	
	out.write("Case #"+str(j)+": "+str(compte))
	print "Case #"+str(j)+": "+str(compte)
	out.write("\n")
	#if j==2:
	#exit()
out.close()
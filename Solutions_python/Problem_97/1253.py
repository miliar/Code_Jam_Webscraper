import sys

def rotateList(num):
	result = []
	snum = str(num)
	l = len(snum)
	
	for i in xrange(l):
		if i == 0:
			nsnum = snum
		else: 
			nsnum = snum[-i:]+snum[:l-i]
		anum = int(nsnum)
		
		#print ">", i, nsnum, anum
		
		#Trailing zero test
		if len(str(anum)) != l:
			continue
		
		if not anum in result: #remove dupes
			result.append(anum)
	
	return result

def count(a, b):

	numbers = []
	for x in xrange(a, b+1):
		rlist = rotateList(x)
		#print "X;", x, "rlist", rlist
		if len(rlist) == 1:
			continue
			
		rlistinrange = []
		for r in rlist:
			if r >= a and r <= b:
				rlistinrange.append(r)
		
		#print "inrange", rlistinrange
		
		if len(rlistinrange) <= 1:
			continue
		
		for r in rlistinrange:
			if not r in numbers:
				numbers.append(r)
		#print "nNumbers", numbers
	
	
	#Oops... did it wrong Fix it here!? D:
	numbers.sort()
	
	partners = 0
	
	while len(numbers) > 0:
		n = numbers.pop()
		rlist = rotateList(n)
		rlist.remove(n)
		
		for r in rlist:
			if r in numbers:
				#numbers.remove(r)
				partners += 1
	
	return partners
		
		
	
	
	return len(numbers)
			

	
a = 1032
b = 1234

print a, rotateList(a)
print b, rotateList(b)

#print "1, 9", count(1, 9)
#print "1, 40", count(10, 40)
#print "100, 500", count(100, 500)
#print "1111, 2222", count(1111,2222)
#print "1, 2000000", count(1111,2000000)


f = file(sys.argv[1], "r")
fo = file(sys.argv[2], "w")

#fo.write("Output\r\n")
i = 1

for line in f:
	line = line.strip()
	if line == "Input":
		continue
	try:
		int(line)
		continue
	except:
		pass
	
	
	#Do the Magic!
	parts = line.split(" ")
	iparts = []
	for part in parts:
		iparts.append(int(part))
		
	A = iparts[0] # Total Number
	B = iparts[1] #Surpise!
	
		
	
	ans = count(A,B)
	
	fo.write("Case #"+str(i)+": "+str(ans)+"\r\n")
	i += 1

fo.close()
f.close()

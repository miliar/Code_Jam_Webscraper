r=open("A-small-attempt1.in","r")

cases=int(r.readline())

consts="bcdfghjklmnpqrstvwxyz"
vowels="aeiou"

for case in xrange(cases):
	line=r.readline().strip().split()
	name,n=line[0],int(line[1])
	
	val=0
	for start in xrange(len(name)):
		for cnt in xrange(len(name)-start):
			string=name[start:len(name)-cnt]
			if len(string)<n:
				break
			cons=0
			for char in string:
				if char in vowels:
					cons=0
				else:
					cons+=1
				if cons>=n:
					val+=1
					break
	print "Case #"+str(case+1)+":",val
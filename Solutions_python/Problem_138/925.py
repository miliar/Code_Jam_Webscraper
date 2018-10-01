f = open('D-large.in.txt','r')
text_file = open("Output4.txt", "w")
numberOfCase = int(f.readline())

# start
for x in xrange(0,numberOfCase):
	blockNum = int(f.readline())
	Naomi = f.readline()
	Ken = f.readline()
	Naomi = Naomi.strip()
	Ken = Ken.strip()

	n = Naomi.split(' ')
	k = Ken.split(' ')
	#print n, k
	n1 = sorted(n)
	k1 = sorted(k)
	#print n1
	#print k1
	#print min(n1),max(n1)

	war = 0
	kenUsed = []
	for i in n1:
		for j in k1:
			if j > i and (j not in kenUsed):
				#print i, j
				kenUsed.append(j)
				war += 1
				break

	uncheated = blockNum - war
	#print uncheated

	dwar 		= 0
	kenUsed 	= []
	naomiUsed 	= []
	naomiTold 	= []
	naomiChose  = []


	for i in k1:
		for j in n1:
			if j>i and (j not in naomiUsed):
				kenUsed.append(i)
				naomiUsed.append(j)
				dwar += 1
				break

	#print dwar
			
	text_file.write("Case #"+str(x+1)+": "+ str(dwar) +" "+ str(uncheated)+"\n")















text_file.close()
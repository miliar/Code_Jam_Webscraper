
import sys

with open(sys.argv[1]) as f:
	content = f.readlines()
testcases = int(content[0].replace('\n',''))
print testcases
counter = 0
f=open('outfile','w')
for i in range(testcases):
	counter = counter + 1
	test = content[counter].replace('\n','').split(' ')
	a,b,k = [int(s) for s in test]
	

	lena = range(a)
	lenb = range(b)
	foo = 0
	print i
	for ii in lena:
		#print ii
		for j in lenb:
			combo = ii & j
			if combo<k:
				foo = foo+1
	f.write('Case #'+str(i+1)+': %d\n'% foo ) 
	


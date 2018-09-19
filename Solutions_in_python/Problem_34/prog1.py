import sys
import string


l=sys.stdin.readline().split()
L,D,N=map(int,l)
#print L,D,N


lWords=[]
for x in range(0,D):
	lWords+=[sys.stdin.readline().strip()]
	

	"""lWords=""""""
abc
bca
dac
dbc
cba
"""


	#lWords=lWords.split('\n')
	#lWords=filter((lambda x: x!=''),lWords)
	#print lWords

for n in range(1,N+1):
	sexp=sys.stdin.readline().strip()
	exp=[]
	while sexp!='':
		if sexp[0]=='(':
			indexOfClose=sexp.find(')')
			head=sexp[1:indexOfClose]
			tail=sexp[indexOfClose+1:]
			sexp=tail
			exp.append(head)
		else:
			exp.append(sexp[0])
			sexp=sexp[1:]
			
	
	
	
	
	#exp=[['a','b','c'],['a','b','c'],['a','b','c']]
	
	filteredList=[]
	filteredList[:]=lWords[:]
	for iteWord in range(0,L):
		l=[]
		for c in exp[iteWord]:
			#print 'currentflist',filteredList,c,iteWord
			l+=filter((lambda x: c==x[iteWord]),filteredList)
			#print 'appended'
		
		#print l
		filteredList=l
	
	print 'Case #%s: %s'%(n, len(filteredList))



import sys

def saisi(f):	
	stock=""
	row=[]
	read = f.readline().rstrip('\n\r')
	for e in read :
		if e != " " :
			stock =stock+e
		else :
			stock = float(stock)
			row.append(stock)
			stock=""
	stock = float(stock)
	row.append(stock)
	return row
def suite(C,F,X,rang):
	somme=0
	const=2
	for i in range(0,rang+1):
		somme = somme + (C/const)
		const=F+const
	return somme
def total(suite,rang,F,X,C):
	const=2
	somme=suite
	nb=0
	for i in range(0,rang):
		const=F+const
	somme=somme+(X/const)
	return somme
def compare(C,F,X):
	rang=0
	while total(suite(C,F,X,rang-1),rang,F,X,C)>total(suite(C,F,X,rang),rang+1,F,X,C) :
		rang=rang+1
	return total(suite(C,F,X,rang-1),rang,F,X,C)
s= open("B-small-attempt0.out",'w')
f = open("B-small-attempt0.in",'r')
entree = int(f.readline())
for x in range(0,entree):
	info = saisi(f)
	a=str(compare(info[0],info[1],info[2]))
	a=a.strip()
	b=str(x+1)
	b=b.strip()
	s.write('Case #'+b+": "+a+'\n')
f.close()
s.close()


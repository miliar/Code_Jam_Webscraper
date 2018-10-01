import sys
def saisi(f):	
	square=[]
	stock=""
	for e in range(0,4) :
		row=[]
		read = f.readline().rstrip('\n\r')
		for e in read :
			if e != " " :
				stock =stock+ e
			else :
				stock = int(stock)
				row.append(stock)
				stock=""
		stock = int(stock)
		row.append(stock)
		stock=""
		square.append(row)
	return square
def extract(select,tab):
	return tab[select]
def researchIndex(e,tab):
	for i in range(0,len(tab)):
		if tab[i]==e :
			return i
	return -1
def fixPoint(row1,row2,select1,select2) :
	stock=[]
	for e in row1 :
		if e in row2:
			stock.append(e)

	if len(stock)==0:
		return "Volunteer cheated!"
	elif len(stock)>=2 :
		return "Bad magician!"
	else :
		st = str(stock[0])
		st= st.strip()
		return st
def org(f,x):
	select1=int(f.readline())
	tab1=saisi(f)
	select2=int(f.readline())
	tab2=saisi(f)
	row1=extract(select1-1,tab1)
	row2=extract(select2-1,tab2)
	a=str(x+1)
	a=a.strip()
	s.write('Case #'+a+": "+fixPoint(row1,row2,select1-1,select2-1)+'\n')

s= open("A-small-attempt6.out",'w')
f = open("A-small-attempt6.in",'r')
entree = int(f.readline())
for x in range(0,entree):
	org(f,x)
f.close()
s.close()







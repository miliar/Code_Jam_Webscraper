
def gana(m,a):
	posi=-1
	i=0
	while i<4:
		j=0
		while j<4:
			if m[i][j]=='T':
				m[i][j]=a
				posi=i
				posj=j			
			j=j+1
		i=i+1
	
	if m[0][0]==a and m[0][1]==a and m[0][2]==a and m[0][3]==a:
		sol=True
	elif m[0][0]==a and m[1][0]==a and m[2][0]==a and m[3][0]==a:
		sol=True
	elif m[3][3]==a and m[2][3]==a and m[1][3]==a and m[0][3]==a:
		sol=True
	elif m[3][3]==a and m[3][2]==a and m[3][1]==a and m[3][0]==a:
		sol=True
	elif m[0][0]==a and m[1][1]==a and m[2][2]==a and m[3][3]==a:
		sol=True
	elif m[3][0]==a and m[2][1]==a and m[1][2]==a and m[0][3]==a:
		sol=True
	elif m[1][0]==a and m[1][1]==a and m[1][2]==a and m[1][3]==a:
		sol=True
	elif m[2][0]==a and m[2][1]==a and m[2][2]==a and m[2][3]==a:
		sol=True
	elif m[0][1]==a and m[1][1]==a and m[2][1]==a and m[3][1]==a:
		sol=True
	elif m[0][2]==a and m[1][2]==a and m[2][2]==a and m[3][2]==a:
		sol=True
	else:
		sol=False

	if posi!=-1:
		m[posi][posj]='T'
	return sol

def empate(m):
	i=0
	while i<4:
		j=0
		while j<4:
			if m[i][j]=='.':
				return False		
			j=j+1
		i=i+1
	return True
	


import sys
if(len(sys.argv) > 1):
	fichero = sys.argv[1]
else: 
	print "Debes indicar el nombre del archivo"

f = open(fichero, "r")
outf= open("sol.txt","w")
casos=int(f.readline())
i=1
while i<=casos:
	fila1=f.readline()
	fila2=f.readline()
	fila3=f.readline()
	fila4=f.readline()
	estado=[list(fila1[0:-1]),list(fila2[0:-1]),list(fila3[0:-1]),list(fila4[0:-1])]
	
	if gana(estado,'X'):
		outf.write("Case #%s: X won" % i)
	elif gana(estado,'O'):
		outf.write("Case #%s: O won" % i)
	elif empate(estado):
		outf.write("Case #%s: Draw" % i)
	else:
		outf.write("Case #%s: Game has not completed" % i)
	if i<casos:
		outf.write("\n")
	f.readline()
	i=i+1

class fichier:
	def __init__(self,path):
		self.path = path
		self.fichier = None

	def open(self,option):
		try:
			self.fichier = open(self.path,option)
		except:
			print("Error File doesn't exist !!!")

	def close(self):
		f.fichier.close()

	def read(self):
		self.open('r')
		text = self.fichier.read()
		self.close()
		return text

	def write(self,text):
		self.open('a')
		self.fichier.write(str(text))
		self.close()

	def new_line(self):
		self.write('\n')
f=fichier("B-large.in")
fout=fichier("outB.out")
t=f.read()
l=t.split("\n")
n=int(l[0])
for i in range(n):
	nbr_max=0
	nbr_surpr=0
	stri=l[i+1]
	list=stri.split(" ")
	nbr_part=int (list[0])
	surp = int (list[1])
	p = int (list[2])
	min=3*p -4
	for j in range(nbr_part):
		if (int(list[j+3]) >= min+2):
			nbr_max=nbr_max+1
		else:
			if (int(list[j+3]) >= min ) and int(list[j+3]) >=p:
				nbr_surpr=nbr_surpr+1
	
	if (surp >= nbr_surpr):
		nbr_max=nbr_max+nbr_surpr
	else:
		nbr_max=nbr_max+surp
	
	fout.write("Case #")
	fout.write(str(i+1))
	fout.write(": ")
	fout.write(str(nbr_max))
	fout.write("\n")


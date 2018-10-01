import os
# Classe Gestion de fichier
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

list1=["y","n","f","i","c","w","l","b","k","u","o","m","x","s","e","v","z","p","d","r","j","g","t","h","a","q"]

list2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


f=fichier("A-small-attempt0 (1).in")
fout=fichier("out.out")
t=f.read()
l=t.split("\n")

n=int (l[0])

for i in range(n):
	stri=l[i+1]
	stri1=''
	for j in range(len(stri)):
		carac=stri[j]
		if carac == " ":
			stri1=stri1 + " "
		else:
			ind = list1.index(carac)
			stri1=stri1 + list2[ind]
	fout.write("Case #")
	fout.write(str(i+1))
	fout.write(": ")
	fout.write(stri1)
	fout.write("\n")
		
		



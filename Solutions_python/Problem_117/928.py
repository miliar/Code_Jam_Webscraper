import os
import operator
import psyco
psyco.full()
#===========================================================================
#                                                Classe Fichier
#===========================================================================
class Fichier:
	def __init__(self,path):
		self.path = path
		self.fichier = None

	def open(self,option):
		try:
			self.fichier = open(self.path,option)
		except:
			print("Error File doesn't exist !!!")

	def read(self):
		self.open('r')
		text = self.fichier.read()
		self.fichier.close()
		return text

	def write(self,text):
		self.open('a')
		self.fichier.write(str(text))
		self.fichier.close()
		
	def new_line(self):
		self.write('\n')
		
	def delete(self):
		self.open('w')
		self.fichier.close()


#===========================================================================
#                                                Traitement
#===========================================================================		

def traitement(input,deb,taille):
	resultat='YES'

	for j in range(deb,int(taille)+deb):
		#print "--------"
		
		sor=sorted(enumerate(input[j]), key=operator.itemgetter(1))
		#print sor
		pu=max(sor, key=lambda x: x[1])
		new_input=list('')
		#print pu
		for i in range(len(sor)):
			if  sor[i][1] != pu[1]:
				new_input.append(sor[i])
		#print new_input		
		# c bon
		if not new_input:
			pass
		else:
			colonne=pu[0]
			for b in new_input:
				for y in range(deb,int(taille)+deb):
					if y != j:
						if input[y][b[0]]>b[1]:
							resultat='NO'
							break
					
		
		

	# Ecriture dans l'output
	
	output.write (resultat)
	output.new_line()




#===========================================================================
#                                                 Main program 
#===========================================================================


file=Fichier("input.in")                            # Ouverture du fichier Input
output=Fichier("output.in")               # Ouverture du fichier Ouput
output.delete()                                    # On efface le contenu du Ouput
r=file.read()                                        
input=r.split("\n")	
l=int(input[0])   	      # nombre de cas a traiter
for i in range(len(input)):
	u=input[i]
	input[i]=u.split(" ")
	for j in range(len(input[i])):
	
		input[i][j]=int(input[i][j])


debut_cas=1
cas=1
while (cas <= l):
	
	output.write("Case #"+str(cas)+": ")
	a=input[debut_cas]
	
	traitement(input,debut_cas+1,a[0])
	debut_cas=debut_cas+int(a[0])+1 # Debut du cas suivant
	cas=cas+1
	


	







	





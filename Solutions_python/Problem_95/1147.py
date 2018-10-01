# !/usr/bin/python
# -*- coding: utf-8 -*-

fichier=open("exemple.txt","r")
fichier.readline()
#print fichier.readline()
fichier2=open("traduction.txt")

code=[]
for line in fichier:
	code.append(line[:len(line)-1])
clair=[]
for line in fichier2:
	clair.append(line[:len(line)-1])
	


dictionnaire={}
for i in range(len(code)):
	for j in range(len(code[i])):
		dictionnaire[code[i][j]]=clair[i][j]
		
for x in dictionnaire:
	print x+" : "+dictionnaire[x]
	
dictionnaire["z"]="q"
dictionnaire["q"]="z"

fichier3=open("input.txt","r")
fichier4=open("solution.txt","w")

fichier3.readline()
compteur=1
for line in fichier3:
	fichier4.write("Case #"+str(compteur)+": ")
	for i in range(len(line)-1):
		fichier4.write(dictionnaire[line[i]])
	fichier4.write("\n")
	compteur+=1


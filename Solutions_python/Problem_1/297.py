#!/usr/bin/env pythonw
# -*- coding:Utf-8 -*-

import sys
import random
from math import *

def findNext(l,index):
	out = []
	rest = len(l)
	while rest :
		for i in range(0,len(l)):
			#print "index : " + str(index) + " i : "+str(i) 
			if (not l[i][index]==0) and not out.count(i):
				rest = rest - 1
				out.append(i)
				#print "Fin de : " + str(i) + " à index = " + str(index) + " reste : " + str(rest)
				if(rest == 0):
					return index
		index = index + 1
		if (index == len(l[0])):
			return index
		
def goDown(l):
	i = 0
	cpt = 0
	while  i < len(l[0]):
		i = findNext(l,i)
		cpt = cpt + 1
		#print "plop"
	return cpt-1

file = open ("a2.dat","r")
f = open("out.dat","w")
N = int(file.readline())
#print N
for i in range(0,N):
	s=[]
	q=[]
	S = int(file.readline()) #Nombre de moteurs de recherche
	#print S
	for j in range (0,S):
		s.append(file.readline())
	Q = int(file.readline()) # Nombre de query
	#print Q
	for j in range (0,Q):
		q.append(file.readline())
	
	l = S*[0]
	for j in range(len(l)):	l[j] = Q*[0] # Tableau de taille S*Q
	
	for k, w in enumerate(q):
		for j, v in enumerate(s):
			if v == w :
				l[j][k]=1
	if not Q==0 :
		resultat = goDown (l)
	else :
		resultat = 0
	print "Case #"+str(i+1)+": "+str(resultat)
	f.write("Case #"+str(i+1)+": "+str(resultat)+"\n")
	
	
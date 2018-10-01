#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import itertools

casesnumber=int(raw_input())
numerodocaso=1

#print casesnumber

lista=list()

while (numerodocaso<=casesnumber):
	linha=raw_input()
	lista.append(linha.split())
	numerodocaso+=1

#print lista

def tidynumber(n):

	#print n 

	index=0
	flag=0

	if (len(n)>1):
		for digito in n:
			if (index+1)<len(n):
				if(n[index]>n[index+1]):
					flag=-1
			index+=1

	return flag

numerodocaso=1

for linha in lista:
	print "Case #%d:"%numerodocaso,
	numerodocaso+=1
	#print linha
	
	numero=linha[0]
	#print numero

	maior=''

	for contador in xrange(int(numero)+1):
		#print contador
		contador=str(contador)
		res=tidynumber(contador)
		if (res==0):
			#print contador
			maior=contador

	print maior
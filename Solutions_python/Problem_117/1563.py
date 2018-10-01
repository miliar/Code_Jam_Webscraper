#!/usr/bin/python
# -*- coding: utf-8 -*-

def thereIsAFalseOnColonne(herbe_plus_basse, colonne, nbLignes):
	for ligne in range(nbLignes):
		if not herbe_plus_basse[ligne][colonne]:
			return True
	return False


def thereIsAFalseOnLigne(herbe_plus_basse, ligne, nbColonnes):
	for colonne in range(nbColonnes):
		if not herbe_plus_basse[ligne][colonne]:
			return True
	return False

def hauteur_invalide(herbe_plus_basse, nbLignes, nbColonnes):
	for ligne in range(nbLignes):
		for colonne in range(nbColonnes):
			if herbe_plus_basse[ligne][colonne]:
				if thereIsAFalseOnLigne(herbe_plus_basse,ligne,nbColonnes) and thereIsAFalseOnColonne(herbe_plus_basse,colonne,nbLignes):
					return True
	return False

inputFile = open("B-small-attempt0.in","r")
solution = open("B-small-attempt0.out","w")

T = int(inputFile.readline().split("\n")[0])

for i in range(T):
	ligne = inputFile.readline()
	N,M = int(ligne.split(" ")[0]), int(ligne.split(" ")[1])

	terrain = []
	hauteurs = []
	for j in range(N):
		ligne = inputFile.readline().split("\n")[0]
		terrain.append(ligne.split(" "))
		for hauteur in terrain[j]:
			if hauteur not in hauteurs:
				hauteurs.append(hauteur)

	reponse = "YES"
	for hauteur in hauteurs :
		herbe_plus_basse = []
		for j in range(N):
			ligne = []
			for k in range(M):
				ligne.append(terrain[j][k] <= hauteur)
			herbe_plus_basse.append(ligne)
		if hauteur_invalide(herbe_plus_basse,N,M):
			reponse = "NO"
			break

	solution.write("Case #"+str(i+1)+": "+reponse+"\n")
	print reponse

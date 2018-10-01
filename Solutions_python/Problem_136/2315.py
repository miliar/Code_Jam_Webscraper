#!/usr/bin/env python3

def meilleur(C, F, X):
	R = 2.0
	derniere_ferme = 0.0
	meilleur = X / R

	while True:
		derniere_ferme += C / R
		R += F
		candidat = derniere_ferme + X / R

		if candidat < meilleur:
			meilleur = candidat

		else:
			break

	return meilleur

T = int(input())

for i in range(T):
	C, F, X = map(float, input().split())
	print("Case #{}: {}".format(i + 1, meilleur(C, F, X)))

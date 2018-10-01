# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:19:55 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Bathroom Stalls')

file = open("C-small-1-attempt0.in",'r')
text = file.read()
monfichier = open("output_small1.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])


def get_info (line):
    S = int(line.split(' ')[0])
    K = int(line.split(' ')[1])
    return S, K

def graph (S):
    bath = ['o']
    for i in range (0,S):
        bath.append('.')
    bath.append('o')
    return bath


    
bath = ['o','.','.','.','o','o','.','.','.','.','.','.','o','.','o']


def longueur_indice (bath):
    longueur_indice = {}
    longueur = 0
    for i in range (len(bath)):
        if bath[i] == '.':
            longueur = 1
            for j in range (i+1,len(bath)):
                if bath[j] == '.':
                    longueur += 1
                else:
                    break
        longueur_indice [i] = longueur
        longueur = 0
    return longueur_indice
        
def indiceOfLongest (bath):
    long_ind = longueur_indice(bath)
    longest = 0
    indice = 0
    for ind in long_ind:
        if long_ind[ind] > longest:
            indice = ind
            longest = long_ind[ind]
    return indice,longest
       
#print(bath)
#print(indiceOfLongest(bath)) 


def placement(bath):
    Ls = 0
    Rs = 0
    indice, longest = indiceOfLongest(bath)
    if longest % 2 != 0:
        indice_choisi = longest//2 + indice
        bath[indice_choisi] = 'o'
        Ls = Rs = longest//2
        
    else:
        indice_choisi = longest//2 + indice - 1
        
        bath[indice_choisi] = 'o'
        Ls = indice_choisi - indice
        Rs = (indice+longest-1) - indice_choisi
        
    return bath, Ls, Rs

def calcul(ligne):
    S,K = get_info(ligne)
    bath = graph(S)
    while K != 0:
        bath,Ls,Rs = placement(bath)
        #print(bath)
        K -= 1
    minimum = min(Ls,Rs)
    maximum = max(Ls,Rs)
    return bath, maximum, minimum
    


#b, l, r = placement (bath)          
#print(b)
#print(l,r)

#ligne = "1000 1"
#b,m,M = calcul(ligne)
#
#print(m,M)

def main():
    for cases in range (1,number_of_cases+1):
        _, outmax, outmin = calcul(lines[cases])
        monfichier.write("Case #"+str(cases)+':'+' '+str(outmax)+' '+str(outmin)+"\n")
        
main()
        
        
            
     
     
     
     
     
     
     
     
     
monfichier.close()
file.close()    
     
     
     
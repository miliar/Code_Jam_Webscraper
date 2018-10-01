# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:38:04 2015

@author: Manence
"""

import numpy as np

def readFile(filename, path):
    fic = open(path+"/"+filename, "r")
    line = fic.readline()
    liste = []
    while(line != ''):
        line = fic.readline()
        try:
            maxShy, people = line.split()
        except ValueError:
            continue
        l = np.zeros(np.int(maxShy)+2, int)
        cpt = 0
        l[cpt] = np.int(maxShy)
        for i in people:
            cpt+=1
            l[cpt] = np.int(i)
        liste.append(l)
    return np.array(liste)
            
def solve(tab):
    tabRes = []
    for i in range(len(tab)):
        popTotalToAdd=0
        for j in xrange(len(tab[i])-1, 0, -1):
            s = 0
            for k in xrange(len(tab[i])-(len(tab[i])-j), 0, -1):
                s+=tab[i][k]
            if(s>j):
                continue
            else:
                nbPopToAdd=j-s
                popTotalToAdd+=nbPopToAdd
                cpt=1
                count = 0
                while(count != nbPopToAdd):
                    if(tab[i][cpt] < 9):
                        tab[i][cpt]+=1
                        count+=1
                    else:
                        cpt+=1
        tabRes.append("Case #"+str(i+1)+": "+str(popTotalToAdd))
    return np.array(tabRes)
            
def writeFile(tabRes, filename, path):
    monFichier = open(path+"/"+filename, "w")
    for i in range(len(tabRes)):
        monFichier.writelines(tabRes[i]+"\n")
    monFichier.close()

path = "C:/Users/Manence/Desktop/jamcode"
filename = "A-large.in"
filenameRes = "resEx1Large.txt"

f = readFile(filename, path)

fRes = solve(f)

writeFile(fRes, filenameRes, path)

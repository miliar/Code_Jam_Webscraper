#! /usr/bin/python -tt
# -*- coding: utf-8 -*-



f = open('workfile','r')
fout = open('file_out','w')

num_test = int((f.readline()).strip())



for m in range(0,num_test):
    
    entree = f.readline()
    C = float((entree.split())[0])
    F = float((entree.split())[1])
    X = float((entree.split())[2])

    n = 0
    somme = 0
    while (X/(2+F*n) >= X/(2+F*(n+1)) + C/(2+F*n)):
        somme += C*1/(2+F*n)
        n += 1
    somme += X/(2+F*n)

    print somme
    fout.write("Case #"+ str(m+1) +": "+ str(somme)+"\n")


    

    
    

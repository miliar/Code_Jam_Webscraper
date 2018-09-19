'''
Created on 11/04/2015

@author: rogerrue
'''

import numpy as np
import random as rnd
from math import sqrt
from reportlab.lib.colors import cadetblue


def llegeixFitxer(fitxer="C-small-attempt0.in"):
    linies = [(lin.strip()).split("\n") 
              for lin in (open(fitxer).readlines())]
    # creo un diccionari amb una entrada per a cada web
    return linies

def liniesAnum(linies):
    tmp = []
    k = 0
    for lini in linies:
        for lin in lini:
            novalin = lin.strip().split(" ")
            if(k==0 or (k%2!=0)):
                for k in range(len(novalin)):
                    novalin[k] = int(novalin[k])
            tmp.append(novalin)
        k += 1
    return tmp

def multiplica(x,y):
    table = { 'i': {'i':'-1', 'j':'k', 'k':'-j'},
             'j': {'i':'-k', 'j':'-1', 'k':'i'},
             'k': {'i':'j', 'j':'-i', 'k':'-1'}}
    sign = 1
    absx = x
    absy = y
    if(y==''):
        return x
    if(x[0]=='-'):
        sign *= -1
        absx = x[1]
    if(y[0]=='-'):
        sign *= -1
        absy = y[1]
    value = '';        
    if(absx=='1'):
        value = absy
    elif (absy=='1'):
        value = absx
    else:
        value = table[absx][absy]
    if(sign==-1):
        if(value[0]=='-'):
            value = value[1]
        else:
            value = '-'+value
    return value

def redueix(llista):
    if(len(llista)==0):
        return ['1']
    while(len(llista)>1):
        result = multiplica(llista[0],llista[1])
        llista.remove(llista[0])
        llista[0] = result
    return llista
    
linies = llegeixFitxer()
linies = liniesAnum(linies)
casos = linies[0][0]
k = 1
find = ['i', 'j', 'k']
for i in range(casos):
    tofind = 0
    found = 0
    L = linies[2*k-1][0]
    X = linies[2*k-1][1]
    cad = linies[2*k][0]
    llargada = L*X
    cadena = cad
    if(X>1):
        for j in range(X-1):
            cadena += cad
    c = 0
    if(len(cadena)<3):
        print 'Case #'+str(k)+': NO'
    elif (len(cadena)==3):
        if(cadena=='ijk'):
            print 'Case #'+str(k)+': YES'
        else:
            print 'Case #'+str(k)+': NO'
    else:
        cars = []
        trobat = []
        for j in range(len(cadena)):
            cars.append(cadena[j])
        while(len(cars)>1 and tofind<3):
            result = multiplica(cars[0],cars[1])
            cars.remove(cars[0])
            cars[0]=result
            if(cars[0]==find[tofind]):
                trobat.append(cars[0])
                tofind += 1
                cars.remove(cars[0])
        resta = redueix(cars)
        if(tofind==3 and resta[0]=='1'):
            print 'Case #'+str(k)+': YES'
        else:
            print 'Case #'+str(k)+': NO'
    k += 1

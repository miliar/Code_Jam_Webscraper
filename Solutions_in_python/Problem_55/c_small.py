from __future__ import division
import sys
import os


arquivo = open('c_small.in','r')
saida = open('c_small.out', 'w')


quantos = int(arquivo.readline())

for i in range(1, quantos+1):
    #print arquivo.readline()
    rides, size, groups = [int(x) for x in arquivo.readline().split()]
    fila = [int(x) for x in arquivo.readline().split()]
    euros = 0
    
    for j in range(0, rides):
    
        in_ride = []
        
        while sum(in_ride) <= size and fila and sum(in_ride)+fila[0] <= size:
            in_ride.append( fila.pop(0) )
        
        euros += sum(in_ride)
        fila.extend(in_ride)
    
    saida.write('Case #%i: %i\n' % (i, euros))

arquivo.close()
saida.close()
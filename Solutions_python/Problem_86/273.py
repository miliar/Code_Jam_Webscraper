#!/usr/bin/env python2.6
#encoding=utf-8
import sys
from math import *
   
def resolve(min, max, notes) :
    encore = True

    for i in xrange(min, max+1) :    
#        if encore :
                 
        
        for note in notes :
        
            c = float(i)/int(note)
#            print "note: %s   | i: %s" % (note, i)
            
#            print c
            if c == int(c) :
#                print "ok, on continue"
                win = i
            elif (int(note)/ float(i)) == int(int(note)/ i) :
                win = i
#                print "Ok, on continue"
            else :
#                print "non"
                win = False
                encore = False
                break
                
        if win :
#            print win
            return win
#        else :
#            print "FINI"
#            break


fichier = open(sys.argv[1], "r")

nb_case = int(fichier.readline().strip("\n"))

for i in xrange(1, nb_case+1) :
    ligne = fichier.readline().split()

#    print ligne
    
    n = ligne[0]
    min = ligne[1]
    max = ligne[2]
    

    notes = fichier.readline().split()
#    print "notes: ", notes
    
    res = resolve(int(min), int(max), notes)
    
    if res :
    
        print "Case #%d: %d" % (i, res)
    else :
        print "Case #%d: NO" % i
    
#    print "----------------------------"

    
fichier.close()

#
# Code by Fernando Gil <http://www.fernandogil.com.br> for Google Code Jam 2013
#
# Use:
# $python bullseye.py sample.in
#
#
import sys,math

def consume(smallRadius, twoR):
    return (smallRadius+1)*(smallRadius+1) - smallRadius*smallRadius + twoR
      
# MAIN

state = 0
line = 0

filename = sys.argv[1]
file = open(filename, 'r')

cases = int(file.readline()) # cases line

for case in range(1,cases+1):
    sys.stdout.write('Case #%d: ' % case)
    
    (strR,strT) = file.readline().split(" ")
    r = int(strR)
    t = int(strT)
    circles = 0
    radius = 0
    twoR = 2 * r
    
    while t > 0:
        circles = circles + 1
        used = consume(radius,twoR)
        t = t - used
        radius = radius + 2
        
    if t < 0:
        circles = circles - 1
    
    sys.stdout.write('%d\n' % circles)
        
#file.readline() # blank line    
    
'''
Created on 12/04/2014

@author: Javier
'''
import copy

fileN = "D-large.in";

inpF = open(fileN, "r")

cases = {}
totalCases = -1
current = 0
blocks = -1

for line in inpF:
    line = line.strip()
    
    if totalCases == -1:
        totalCases = int(line)
        continue
    
    
    if blocks == -1:
        blocks = int(line)
        tmpO = {
                'n': [],
                'k': []
        }
        
        cases[current] = tmpO
        
        continue
    
    
    data = line.split(" ")
    if len(data) == blocks:
        
        lTadd = cases[current]['n']
        
        if len(cases[current]['n']) != 0:
            lTadd = cases[current]['k']
            current += 1
            blocks = -1
            
        for x in data:
            lTadd.append(float(x))
            
        
def war(blocks):
    #sort arrays
    blocks['n'].sort()
    blocks['k'].sort()
    points = 0
    
    for i in range(len(blocks['k'])):
        
        naomi = blocks['n'][0]
        
        # ken select bigger block that naomi if it possible
        ken = blocks['k'][0]
        for y in blocks['k']:
            if y > naomi:
                ken = y
                break
        
        if naomi > ken:
            points += 1
        
        blocks['n'].remove(naomi)
        blocks['k'].remove(ken)
        
    return points

def deceitful(blocks):
    #sort arrays
    blocks['n'].sort()
    blocks['k'].sort()
    points = 0
    
    for i in range(len(blocks['k'])):
        
        naomi = blocks['n'][0]
        
        
        #siempre y cuando tenga una mayor que su menor
        tengoMayor = False
        #le digo tengo mas grande que todas las de el
        #lanzo una mayor a su menor para cumplir
        #el usara la mas pequena
        for y in blocks['n']:
            if y > blocks['k'][0]:
                tengoMayor = y
                break
        
        if tengoMayor:
            bigKen = len(blocks['k']) - 1
            bigKen = blocks['k'][bigKen];
            
            diff = (1.0 - bigKen) / 2;
            naomiTell = bigKen + diff
            
            naomi = tengoMayor
        else:

            # si no usar el menor para matar su mayor bloque
            
            bigKen = len(blocks['k']) - 1
            bigKen = blocks['k'][bigKen];
            
            
            prevKen = len(blocks['k']) - 2
            if prevKen < 0:
                prevKen = 0.0
            else:
                prevKen = blocks['k'][prevKen]
            
            #less that bigKen more that prevKen
            naomiTell = bigKen
    
            toRest = (bigKen - prevKen) / 2;
            naomiTell -= toRest
            if naomiTell < naomi:
                naomiTell = naomi
        
        
        
        # ken select bigger block that naomi if it possible
        ken = blocks['k'][0]
        for y in blocks['k']:
            if y > naomiTell:
                ken = y
                break
        
        if naomi > ken:
            points += 1
        
        blocks['n'].remove(naomi)
        blocks['k'].remove(ken)
        
    return points

for i in cases:
    y = deceitful(copy.deepcopy(cases[i]))
    z = war(cases[i])
    
    print "Case #" + str(i + 1) + ": " + str(y) + " " + str(z)
    
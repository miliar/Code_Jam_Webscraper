def zmen(prikaz,systemy,prikazy):
    max = 0
    id = 0
    akt = 0
    
    for i in xrange(len(systemy)): 
        
        akt = 0
        
        if prikaz <> systemy[i]:
        
            for o in xrange(len(prikazy)):
                if prikazy[o] == systemy[i]:
                    break
                akt += 1
                
                
                
        if akt >= max:
            max = akt
            id = i
            
    return systemy[id]

def vypocet(systemy,prikazy):
    zmien = 0
    akt = zmen('',systemy,prikazy) # Posledne pouzity system
    
    while len(prikazy) > 0:
        prikaz = prikazy[0]
        if akt == prikaz:
            zmien += 1
            akt = zmen(prikaz,systemy,prikazy)
        prikazy.pop(0)
            
    return zmien


#Nacitanie dat
pokusov = int(raw_input())
for i in xrange(1,pokusov+1):
    systemy = [] # Pole systemov
    prikazy = [] # Pole prikazov
    
    systemov = int(raw_input())
    
    for o in xrange(systemov):
        input = raw_input()
        systemy.append(input)
   
    prikazov = int(raw_input())
    
    for o in xrange(prikazov):
        input = raw_input()
        prikazy.append(input)
    
    print 'Case #' + str(i) + ': ' + str(vypocet(systemy,prikazy))
        
    

from copy import copy

class Planet :
    def __init__ (self, val):
        self.v = val
        self.threatened = False
        self.threat = set([])
        self.step = 10000000000000000


def relax (planet1, planet2):
    if planet1.step < 100000:
        if planet2.step > planet1.step + 1:
            planet2.step = planet1.step +1
            planet2.parent = planet1.value
            planet2.threat = planet1.threat.union(planet2.neighbors)
            planet2.conquer = copy(planet1.conquer)
            planet2.conquer.add(planet2.value)
            planet2.threat = planet2.threat.difference(planet2.conquer)
            #print ('relaxed :', planet2.value, planet2.parent, planet2.conquer, planet2.threat)
            planet2.step = planet1.step+1
        if planet2.step == planet1.step + 1:
            tmp_conquer = copy(planet1.conquer)
            tmp_conquer.add(planet2.value)
            tmp_threat = copy(planet1.threat)
            tmp_threat = tmp_threat.union(planet2.neighbors)
            tmp_threat = tmp_threat.difference(tmp_conquer)
            if len(tmp_threat) > len(planet2.threat):
                planet2.step = planet1.step +1
                planet2.parent = planet1.value
                planet2.threat = planet1.threat.union(planet2.neighbors)
                planet2.conquer = copy(planet1.conquer)
                planet2.conquer.add(planet2.value)
                planet2.threat = planet2.threat.difference(planet2.conquer)
                planet2.step = planet1.step+1
                #print ('relaxed! :', planet2.value, planet2.parent, planet2.conquer, planet2.threat)
    return




fin = open ('c:/users/hai/my projects/google code jam/2011/2/D/D-small-attempt2.in')
fout = open ('c:/users/hai/my projects/google code jam/2011/2/D/D-small-attempt2.out','w')

T = int(fin.readline())

for testcase in range(1,T+1):
    P,W = [int(x) for x in fin.readline().split()]
    l = fin.readline().split()
    #print ('l:',l)
    l2= []
    for i in l:
        pair = [int(x) for x in i.split(',')]
        l2.append(pair)
    #print (l2)
    d={}
    for i in range(500):
        d[i] = []
    for i,j in l2:
        d[i].append(j)
        d[j].append(i)

    planets = []
    for i in range(P):
        planets.append(Planet(i))
    for i in range(P):
        planets[i].neighbors = set(d[i][:])
        planets[i].parent = None
        planets[i].conquer = set([])
        planets[i].threat = set([])
        planets[i].step = 10000000000000000000000000
        planets[i].value = i
    
        
    conquered = [Planet(0)]
    step = 0
    planets[0].parent = None
    planets[0].threat = set(d[0][:])
    planets[0].step = 0
    planets[0].conquer = set([0])

    stopit = False
    for step in range(5000):
        #print ('step: ',step)
        for p in planets:
            if 1 in p.threat:
                stopit = True
        if stopit:
            break
        for i in d:
            for j in d[i]:
                #planets i,j are connected
                if planets[i].step == step:
                    relax(planets[i],planets[j])
                if planets[j].step == step:
                    relax(planets[j],planets[i])

    best = planets[0]
    for p in planets:
        if len(p.conquer) > len(best.conquer) or (len(p.conquer)==len(best.conquer) and len(p.threat) > len(best.threat)):
            if 1 in p.threat:
                best = p
        
    print (step, len(best.conquer),len(best.threat))  

    fout.write('Case #' + str(testcase) + ': ' + str(len(best.conquer)-1) + ' ' + str(len(best.threat))+'\n')
fin.close()
fout.close()

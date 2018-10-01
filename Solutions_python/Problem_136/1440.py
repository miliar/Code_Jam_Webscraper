'''
Created on Apr 11, 2014

@author: Sean Groathouse
'''

fin = open('B-large.in', 'r')
finput = fin.readlines()
fin.close()

it = iter(finput)

numbCases = int(it.next())

output = ""

for case in xrange(numbCases):    
    [farmCost, farmRate, goal] = [float(j) for j in (it.next()).split()]
    time = float(0.0)
    rate = float(2.0)
    farmsCreated = float(0)
    finished = False       
    
    while (not finished):
        directlyToGoal = goal / rate
        addFactoryFirst = (farmCost / rate) + (goal / (rate + farmRate))
        if (directlyToGoal < addFactoryFirst):
            time = time + directlyToGoal
            finished = True
        else:
            time = time + (farmCost / rate)
            rate = rate + farmRate
            
    minimumTime = str(time)
    
    output += "Case #%d: %s\n" % (case+1, minimumTime)

fout = open('large.txt', 'w')
fout.write(output)
fout.close
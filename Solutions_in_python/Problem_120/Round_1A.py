'''
Created on Apr 26, 2013

@author: RDrapeau
'''

file = open("A-small-attempt0.in", 'r')

cases = int(file.next())

for x in range(1, cases + 1):
    data = file.next().split(" ")
    
    rNot = int(data[0])
    paint = data[1]
    paint = int(paint[:len(paint)])
    
    count = 0
    radius = rNot
    
    while (paint > 0):
        radius += 1
        area = radius ** 2 - (radius - 1) ** 2
        paint -= area
        if (paint >= 0):
            count += 1
        radius += 1
    print "Case #%d: %d" % (x, count)

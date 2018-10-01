f = open('B-large.in', 'r')
g = open('output.txt', 'w')
n = int(f.readline())
for i in range (1, n+1):
    found = 0
    string = f.readline()
    floats = string.split()
    production = 2.0
    C = float(floats[0])
    F = float(floats[1])
    X = float(floats[2])
    time1 = X/production
    time2 = C/production + X/(production+F)
    production = production + F
    while time1 > time2:
    	time1 = time2
    	time2 = time2 - X/(production) + C/production + X/(production+F)
    	production = production + F 
    line = 'Case #' + str(i) + ': ' + str(time1) + '\n'
    g.write(line) 
f.close()
g.close()
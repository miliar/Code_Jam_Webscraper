import string

infile = open("A-large.in",'r')
outfile = open("A-large.out", 'w')

numCases = eval(string.split(infile.readline(), "\n")[0])

for case in range(numCases):
    engines = []
    used = {}
    
    numEngines = eval(string.split(infile.readline(), "\n")[0])
    for i in range(numEngines):
        engines.append(string.split(infile.readline(), "\n")[0])
        
    numQueries = eval(string.split(infile.readline(), "\n")[0])

    switchCounter = 0
    for i in range(numQueries):
        q = string.split(infile.readline(), "\n")[0]

        used[q] = True
        if len(used) >= numEngines:
            switchCounter += 1
            used = {}
            used[q] = True
            
   
    outfile.write("Case #%d: %d\n" % (case + 1, switchCounter))
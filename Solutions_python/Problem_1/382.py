import sets, sys

fh = open("inputs/%s" % sys.argv[1], 'r')
lines = fh.readlines()
engines = sets.Set()

cases = int(lines[0])
index = 1

output = open("outputs/A.out", 'w')
#O(N) in input, O(2N) in memory, could be better
#I spent over 90 minutes combing the input and output before I realized I was starting my case numbers base 0, YAY
for i in range(0, cases):
    engines.clear()    
    engineCount = int(lines[index])
    index += engineCount + 1
    queryCount = int(lines[index])
    index += 1
    queries = lines[index:index+queryCount]
    switchCount = 0
    #print "Engine Count: %s" % engineCount
    count = 0
    for query in queries:
        count += 1
        engines.add(query.rstrip('\n'))
        if len(engines) == engineCount:
            engines.clear()
            engines.add(query.rstrip('\n'))
            switchCount += 1
    output.write("Case #%i: %i\n" % (i+1, switchCount))
    index += queryCount
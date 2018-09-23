import string, math

#inputFile = open('large_input_test.in', 'r')
inputFile = open('express.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
data      = inputData.split('\n')

def formatAnswer(index, answer):
  return "Case #" + str(index) + ": " + str(answer[0])

def addToDict(valDict, key, value):
    if key in valDict:
        valDict[key].add(value)
    else:
        valDict[key] = set([value])

def computeAnswer(horses, distances, route):
    route     = (route[0] - 1, route[1] - 1) # shifting to 0 indexing
    numCities = len(horses)
    results   = dict()

    # tuple(time to get to spot, tuple(horse stamina, speed))
    results[0] = set([(0, horses[0])])

    for city in xrange(1,numCities):
        for time, horse in list(results[city-1]):
            horse = (horse[0]-distances[city-1][city], horse[1])
            if horse[0] < 0:
                continue
            time  = time + distances[city-1][city] *1.0 / horse[1]

            addToDict(results, city, (time,horse))

        bestTime = min([t[0] for t in results[city]])

        addToDict(results, city, (bestTime, horses[city]))

    
    return min([t[0] for t in results[route[1]]])


index = 1
for case in xrange(1, numCases+1):
    numCities, numRoutes  = map(int, data[index].split(" "))

    horses     = map(lambda row: tuple(map(int, row.split(" "))), data[index+1: index+numCities+1])

    distances  = map(lambda row: map(int, row.split(" ")), data[index+numCities+1:index + 2*numCities+1])
    index     += numCities * 2 + 1

    routes     = map(lambda row: map(int, row.split(" ")), data[index:index + numRoutes])
    index     += numRoutes

    answer = []
    for route in routes:
        answer.append( computeAnswer(horses, distances, route))

    print formatAnswer(case, answer)



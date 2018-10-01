import sys

# All friends are sassumed to be of a shyness level of 0
def allStanding (shynessLevels, numberOfFriends) :
    standing = numberOfFriends;
    for i in range(len(shynessLevels)) :
        if standing < i :
            return False
        standing += shynessLevels[i]
    return True

# A rather simple brute force solution.
# Are we supposed to find an efficent solution or just a good enough one? I am not sure.
def minFriends (inputString):
    shynessLevels = map(int, inputString)
    currentGuess = 0
    while not allStanding(shynessLevels, currentGuess):
        currentGuess += 1
    return currentGuess



cases = int(sys.stdin.readline());
for i in range (cases):
    split = sys.stdin.readline().split()
    maxShyness = split[0]
    shynessLevels = split[1]
    print "Case #%d: %s" % (i + 1, minFriends(shynessLevels))

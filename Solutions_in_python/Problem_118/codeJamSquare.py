import math

def isPalindrome(x):
    return str(x)[::-1] == str(x)

def isSquare(x):
    lastDigit = x%10
    if lastDigit == 2 or lastDigit == 3 or lastDigit == 7 or lastDigit == 8:
        return False
    
    sq = math.floor(math.sqrt(x))
    return sq**2 == x


with open("C-small-attempt0.in") as ins:
    content = ins.readlines()
##print content
##print content[0]

numberOfCases = int(content[0])
##print numberOfCases

games = []
for i in range(numberOfCases):
    tup = content[i+1][:-1].split(" ")
##    print content[i+1][:-1].split(" ")
    N = int(tup[0])
    M = int(tup[1])
    games.append([N, M])
##print games

for game in games:
    count = 0
##    print game[0], game[1]
    for i in range(game[0], game[1] + 1):
        if isPalindrome(i) and isSquare(i):
            if isPalindrome(int(math.sqrt(i))):
                count +=1
##                print i
    print "Case #" + str(games.index(game)+1) + ": " + str(count)

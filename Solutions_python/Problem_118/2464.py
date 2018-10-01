import math;

f = open('input3.txt')
lines = f.readlines()
f.close

cases = int(lines[0])
games = []
for x in range(1,cases+1):
    game = lines[x].split()[:2]
    game[0] = int(game[0])
    game[1] = int(game[1])
    games.append(game)

print(games)

outputfile = open("output3.txt", "a")

def isPalindrome(num):
    thing = str(num)
    return (thing == thing[::-1])

def numSquarePalindromes(low, high):
    palindromes = []
    satisfyingpalindromes = []
    roothigh = math.sqrt(float(high))
    roothigh = math.ceil(roothigh)
    roothigh = int(roothigh)
    for x in range(1, roothigh+1):
        if isPalindrome(x):
            palindromes.append(x)
    for x in palindromes:
        if x*x > high:
            return len(satisfyingpalindromes)
        elif x*x >= low and (isPalindrome(x*x)):
            satisfyingpalindromes.append(x**x)
    return len(satisfyingpalindromes)

for x in range(cases):
    outputfile.write("Case #" + str(x+1) + ": " + str(numSquarePalindromes(games[x][0], games[x][1])) + "\n")


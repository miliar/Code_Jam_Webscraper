import math

f = open("C-small-attempt0.in","r")

cases = int(f.readline())

x = 1

def generatePalindromes(low,high):
    palindromes = []
    for i in range(low,high+1):
        if str(i) == str(i)[::-1]:
            palindromes.append(i)

    return palindromes


while x <= cases:

    ints = f.readline().rstrip('\n').split(' ')

    count = 0

    for j in generatePalindromes(int(ints[0]),int(ints[1])):

        ans = (math.sqrt(j))

        if str(ans)[str(ans).index("."):]==".0":
            ans = int(ans)

        if str(ans) == str(ans)[::-1]:
            count += 1

    print "Case #" + str(x) + ": " + str(count)

    x += 1

            

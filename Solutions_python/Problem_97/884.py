def checkValues(x, y):
    total = 0
    for i in range(x, y+1):
        z = i
        j = 1
        while (j <= len(str(i))-1):
            z = str(z)
            if (len(z) < len(str(i))):
                z = '0' + z
            z = z[len(z)-1:len(z)] + z[0:len(z)-1]
            z = int(z)
            if (z >= x and z <= y and z > i):
                total += 1
            j += 1
    return total

def computeValues(x):
    values = x.split(' ')
    minValue = int(values[0])
    maxValue = int(values[1])
    return checkValues(minValue, maxValue)

def main(filename):
    f = open(filename, "r")
    numTestCases = int(f.readline())
    a = open("output3.txt", "w")
    for x in range(1, numTestCases+1):
        testLine = f.readline()
        numValues = computeValues(testLine)
        a.write('Case #' + str(x) + ': ' + str(numValues) + '\n')
    a.close()

main("C-small-attempt0.in")

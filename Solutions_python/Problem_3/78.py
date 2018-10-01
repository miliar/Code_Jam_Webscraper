#!/usr/bin/python2.5

import math

fileNameInput  = 'C-small.in'
fileNameOutput = 'C-small.out'
#fileNameInput  = 'C-large.in'
#fileNameOutput = 'C-large.out'

def integral(R, x1, x2, bottomY):
    if x2 < x1: return 0.0
    if x1 >= R: return 0.0
    if R-x2 <= 0.0: x2 = R-0.000001
    res1 = ( (R**2.0)*(math.atan(x1/math.sqrt(R**2-x1**2))) + (x1*math.sqrt(R**2-x1**2)) )/2.0
    res2 = ( (R**2.0)*(math.atan(x2/math.sqrt(R**2-x2**2))) + (x2*math.sqrt(R**2-x2**2)) )/2.0
    res = res2-res1-bottomY*(x2-x1)
    if res > 0.0: return res
    else: return 0.0

def maxX(R, y):
    if R>=y: return math.sqrt(R**2-y**2)
    else: return None

def min2(l):
    while None in l: l.remove(None)
    return min(l)

def squareArea(x, y, g, f, t, R):
    x1 = x+f
    x2 = min2([x+g-f, maxX(R-t-f, y+f)])
    res1 = integral(R-t-f, x1, x2, y+f)
    x1 = x+f
    x2 = min2([x+g-f, maxX(R-t-f, y+g-f)])
    res2 = integral(R-t-f, x1, x2, y+g-f)
    return res1-res2

def findSolution(f, R, t, r, g):
    # find squares or even parts of them in 1/4 (up, right) of circle
    sqArea = 0.0
    y = r
    while y < R-t:
        x = r
        while x < R-t:
            try:
                addArea = squareArea(x, y, g, f, t, R)
                sqArea += addArea
                x += g+2.0*r
            except ValueError:
                break
        y += g+2.0*r
    # calculate probability and return it
    res = (math.pi*(R**2)-4.0*sqArea)/(math.pi*(R**2))
    return "%.6f" % res


if __name__ == '__main__':
    input = file(fileNameInput, 'r').readlines()
    output = file(fileNameOutput, 'w')

    # filter \n charachters
    for x in xrange(len(input)):
        input[x] = input[x].replace('\r','').replace('\n','')

    numberOfTests = int(input[0])
    line = 1
    for x in xrange(1, numberOfTests+1):
        v = input[x].split()
        solution = findSolution(float(v[0]), float(v[1]), float(v[2]), float(v[3]), float(v[4]))
        output.write('Case #' + str(x) + ': ' + str(solution) + '\n')
    output.close()
    print 'done'

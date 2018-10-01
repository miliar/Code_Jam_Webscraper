import string
import sys
import math
def getline(f):
    return string.split(f.readline(), "\n")[0]


def sign(val):
    if val >= 0:
        return 1
    return -1

class pt():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.len = math.hypot(x,y)
    
    def __abs__(self):
        return self.len
        
        
class Box():
    def __init__(self, topLeft, bottomRight, clipRadius = sys.maxint):
        if topLeft.x > bottomRight.x:
            raise Exception
            return 0
        if topLeft.y < bottomRight.y:
            raise Exception
            return 0
        topRight = pt(bottomRight.x, topLeft.y)
        bottomLeft = pt(topLeft.x, bottomRight.y)
        clipRadius = float(clipRadius)
        self.area = 0
        
        topLeftIn = abs(topLeft) <= clipRadius
        topRightIn = abs(topRight) <= clipRadius
        bottomLeftIn = abs(bottomLeft) <= clipRadius
        bottomRightIn = abs(bottomRight) <= clipRadius        
        
        #Is it completely inside?
        if topLeftIn and topRightIn and bottomLeftIn and bottomRightIn:
            self.area = abs(topLeft.x - bottomRight.x) * abs(topLeft.y - bottomRight.y)
            return

        #Completely outside?
        if not topLeftIn and not topRightIn and not bottomLeftIn and not bottomRightIn:
            self.area = 0
            return
        
        #The remaining case - part of it is outside, part of it insde
        pt1 = None
        pt2 = None
        
        #First Cases - one corner is out
        if not topLeftIn and topRightIn and bottomLeftIn and bottomRightIn:
            pt1 = pt(topLeft.x, sign(topLeft.y) * math.sqrt((clipRadius ** 2) - (topLeft.x ** 2)))
            pt2 = pt(sign(topLeft.x) * math.sqrt((clipRadius ** 2) - (topLeft.y ** 2)), topLeft.y)
            self.area = Box(pt2, bottomRight).area + Box(pt1, pt(pt2.x, bottomRight.y)).area
        
        elif topLeftIn and not topRightIn and bottomLeftIn and bottomRightIn:
            pt1 = pt(topRight.x, sign(topRight.y) * math.sqrt((clipRadius ** 2) - (topRight.x ** 2)))
            pt2 = pt(sign(topRight.x) * math.sqrt((clipRadius ** 2) - (topRight.y ** 2)), topRight.y)
            self.area = Box(topLeft, pt(pt2.x, pt1.y)).area + Box(pt(topLeft.x, pt1.y), bottomRight).area
            
        elif topLeftIn and topRightIn and not bottomLeftIn and bottomRightIn:
            pt1 = pt(bottomLeft.x, sign(bottomLeft.y) * math.sqrt((clipRadius ** 2) - (bottomLeft.x ** 2)))
            pt2 = pt(sign(bottomLeft.x) * math.sqrt((clipRadius ** 2) - (bottomLeft.y ** 2)), bottomLeft.y)
            self.area = Box(topLeft, pt(pt2.x, pt1.y)).area + Box(pt(pt2.x, topLeft.y), bottomRight).area
            
        elif topLeftIn and topRightIn and bottomLeftIn and not bottomRightIn:
            pt1 = pt(bottomRight.x, sign(bottomRight.y) * math.sqrt((clipRadius ** 2) - (bottomRight.x ** 2)))
            pt2 = pt(sign(bottomRight.x) * math.sqrt((clipRadius ** 2) - (bottomRight.y ** 2)), bottomRight.y)
            self.area = Box(topLeft, pt2).area + Box(pt(pt2.x, topLeft.y), pt1).area

        #Second cases - two corners are out
        elif not topLeftIn and not topRightIn and bottomLeftIn and bottomRightIn:
            pt1 = pt(topLeft.x, sign(topLeft.y) * math.sqrt((clipRadius ** 2) - (topLeft.x ** 2)))
            pt2 = pt(topRight.x, sign(topRight.y) * math.sqrt((clipRadius ** 2) - (topRight.x ** 2)))
            self.area = Box(pt(pt1.x, pt2.y), bottomRight).area
            
        elif topLeftIn and not topRightIn and bottomLeftIn and not bottomRightIn:
            pt1 = pt(sign(topRight.x) * math.sqrt((clipRadius ** 2) - (topRight.y ** 2)), topRight.y)
            pt2 = pt(sign(bottomRight.x) * math.sqrt((clipRadius ** 2) - (bottomRight.y ** 2)), bottomRight.y)
            self.area = Box(topLeft, pt(pt1.x, pt2.y)).area

            
        elif topLeftIn and topRightIn and not bottomLeftIn and not bottomRightIn:
            pt1 = pt(bottomLeft.x, sign(bottomLeft.y) * math.sqrt((clipRadius ** 2) - (bottomLeft.x ** 2)))
            pt2 = pt(bottomRight.x, sign(bottomRight.y) * math.sqrt((clipRadius ** 2) - (bottomRight.x ** 2)))
            self.area = Box(topLeft, pt2).area
            
        elif not topLeftIn and topRightIn and not bottomLeftIn and bottomRightIn:
            pt1 = pt(sign(topLeft.x) * math.sqrt((clipRadius ** 2) - (topLeft.y ** 2)), topLeft.y)
            pt2 = pt(sign(bottomRight.x) * math.sqrt((clipRadius ** 2) - (bottomRight.y ** 2)), bottomRight.y)
            self.area = Box(pt1, bottomRight).area
            
        #Third Cases - only one corner is in
        elif topLeftIn and not topRightIn and not bottomLeftIn and not bottomRightIn:
            pt1 = pt(topLeft.x, sign(topLeft.y) * math.sqrt((clipRadius ** 2) - (topLeft.x ** 2)))
            pt2 = pt(sign(topLeft.x) * math.sqrt((clipRadius ** 2) - (topLeft.y ** 2)), topLeft.y)
            self.area = 0
        
        elif not topLeftIn and topRightIn and not bottomLeftIn and not bottomRightIn:
            pt1 = pt(sign(topRight.x) * math.sqrt((clipRadius ** 2) - (topRight.y ** 2)), topRight.y)
            pt2 = pt(topRight.x, sign(topRight.y) * math.sqrt((clipRadius ** 2) - (topRight.x ** 2)))
            self.area = 0
            
        elif not topLeftIn and not topRightIn and bottomLeftIn and not bottomRightIn:
            pt1 = pt(bottomLeft.x, sign(bottomLeft.y) * math.sqrt((clipRadius ** 2) - (bottomLeft.x ** 2)))
            pt2 = pt(sign(bottomLeft.x) * math.sqrt((clipRadius ** 2) - (bottomLeft.y ** 2)), bottomLeft.y)
            self.area = 0
            
        elif not topLeftIn and not topRightIn and not bottomLeftIn and bottomRightIn:
            pt1 = pt(bottomRight.x, sign(bottomRight.y) * math.sqrt((clipRadius ** 2) - (bottomRight.x ** 2)))
            pt2 = pt(sign(bottomRight.x) * math.sqrt((clipRadius ** 2) - (bottomRight.y ** 2)), bottomRight.y)
            self.area = 0
            
        #Compute the area of the circle bit
        angle = abs(math.acos(((pt1.x * pt2.x) + (pt1.y * pt2.y) ) / (abs(pt1) * abs(pt2))))
        self.area += ((clipRadius ** 2) / 2.0 * angle) - ((clipRadius ** 2) * math.sin(angle) / 2.0) + (abs(pt1.x - pt2.x) * abs(pt1.y - pt2.y) / 2.0)

    
infile = open("C-small-attempt0.in", 'r')
outfile = open("C-small.out",'w')
numCases = eval(getline(infile))

for case in range(numCases):
    l = string.split(getline(infile))
    
    flySize = float(eval(l[0]))
    racketRad = float(eval(l[1]))
    racketThick = float(eval(l[2]))
    stringRad = float(eval(l[3]))
    gridSize = float(eval(l[4]))

    circleClip = racketRad - racketThick - flySize
    
    flyArea = 0
    
    x = stringRad
    while x <= racketRad:
        y = stringRad
        while y <= racketRad:
            area = Box(pt(x + flySize, y + gridSize - flySize), pt(x + gridSize - flySize, y + flySize), circleClip).area
            if area > 0:
                flyArea += area
                
            if flyArea * 4 > (math.pi * (racketRad ** 2)):
                raise Exception
            
            y += stringRad * 2 + gridSize

        x += stringRad * 2 + gridSize
        
    flyArea *= 4
    
    prob = 1 - (flyArea / (math.pi * (racketRad ** 2)))
    
    #print "\n\n\nCase #%d: %.6f" % (case + 1, prob)
    outfile.write("Case #%d: %.6f\n" % (case + 1, prob))
    
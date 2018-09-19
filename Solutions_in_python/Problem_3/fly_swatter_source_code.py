##FLY SWATTER##

##Thomas Pollom##

import math

class Hole:
    def __init__(self, coordinate, side_length, Radius):
        """
        """
        self.coordinate = coordinate
        self.side_length = side_length
        self.Radius = Radius
        self.theta = 0.0
        self.area = 0.0
    def getCoordinate(self):
        "Return the hole's coordinate."
        return self.coordinate
    def getSide_length(self):
        "Return the hole's side_length."
        return self.side_length
    def getRadius(self):
        "Return the radius of racket."
        return self.Radius
    def getArea(self):
        "Return the hole's area."
        return self.area
    def setArea(self, area):
        "Sets the hole's area."
        self.area = area
    def calcArea(self):
        "calculates the hole's area"
        if (self.coordinate[0])*(self.coordinate[0]) + (self.coordinate[1])*(self.coordinate[1]) >= (self.Radius)*(self.Radius):
            return 0.0
        if (self.coordinate[0] + self.side_length)*(self.coordinate[0] + self.side_length) + (self.coordinate[1] + self.side_length)*(self.coordinate[1] + self.side_length) <= (self.Radius)*(self.Radius):
            return (self.side_length)*(self.side_length)
        a = 0.0
        b = 0.0
        c = 0.0
        d = 0.0
        e = 0.0
        h = 0.0
        x = self.coordinate[0]
        y = self.coordinate[1]
        R = self.Radius
        t = self.theta
        if (self.coordinate[0] + self.side_length)*(self.coordinate[0] + self.side_length) + (self.coordinate[1])*(self.coordinate[1]) >= (self.Radius)*(self.Radius):
            b = math.sqrt(R*R - y*y) - x
            d = 0.0
        else:
            b = self.side_length
            d = math.sqrt(R*R - (x + b)*(x + b)) - y
        if (self.coordinate[1] + self.side_length)*(self.coordinate[1] + self.side_length) + (self.coordinate[0])*(self.coordinate[0]) >= (self.Radius)*(self.Radius):
            a = math.sqrt(R*R - x*x) - y
            c = 0.0
        else:
            a = self.side_length
            c = math.sqrt(R*R - (y + a)*(y + a)) - x
        e = math.sqrt((b - c)*(b - c) + (a - d)*(a - d))
        h = math.sqrt(R*R - (e/2.0)*(e/2.0))
        t = 2*math.asin(e/(2.0*R))
        hole_area = a*c + b*d - c*d + (b - c)*(a - d)/2.0 + R*R*t/2.0 - e*h/2.0
        return hole_area
    

# Transform file to list.

input_file = open('/Users/scotty/Desktop/input_file3.txt', 'r')
raw_lines = input_file.readlines()
input_file.close()
lines = []
for line in raw_lines:
    line = line.rstrip('\n')
    lines.append(line)

output_file = open('/Users/scotty/Desktop/output_file3.txt', 'w')

# Calculate probability of hitting the fly.
# Assumes correct format for input file.

num_cases = int(lines[0])
current_case = 1
while current_case <= num_cases:
    holes = []
    data = lines[current_case].split()
    f = float(data[0])
    R = float(data[1])
    t = float(data[2])
    r = float(data[3])
    g = float(data[4])
    if 2.0*f >= g:
        prob = 1.0
    else:
        coord_range = int((R)/(g + 2.0*r) + 1)
        for i in range(coord_range):
            for j in range(coord_range):
                new_hole = Hole([(r + f + (g + 2.0*r)*i), (r + f + (g + 2.0*r)*j)], (g - 2.0*f), (R - t - f))
                new_hole_area = new_hole.calcArea()
                new_hole.setArea(new_hole_area)
                holes.append(new_hole)
        total_hole_area = 0.0
        for sample_hole in holes:
            total_hole_area += sample_hole.getArea()
        prob = 1 - total_hole_area/(R*R*3.14159265/4.0)
        if prob < 0.000001:
            prob = 0.0
    output = 'Case #%s: %6f' %(current_case, prob)
    output_file.write(output)
    output_file.write('\n')
    print current_case
    current_case += 1

output_file.close()

print 'done'

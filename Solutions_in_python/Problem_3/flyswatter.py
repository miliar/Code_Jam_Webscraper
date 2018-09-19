import math
import sys
import re

pi = math.pi

def probability(t,f,g,r,R):
    if 2*f>g:
        return 0
    if R-t < f:
        return 0
    totalArea = pi * ((R-t-f)**2)
    x=-(g+2*r)
    sa=0
    while True:
        if x-r < -(R-t):
            break
        stringa =  stringArea(x, r+f, (R-t-f))
        sa+=stringa
        x-=g+2*r
    sa*=4
    sa+=2*stringArea(0, r+f, (R-t-f))
    x=-g-2*r
    duparea = 0
    while True:    
        if x-r <= -(R-t):
            break
        y=-g-2*r
        while True:
            if y-r <= -(R-t):
                break
            val = find_intersection_area(x,y,(R-t-f), r + f)
            duparea += val
            y-=g+2*r
        x-=g+2*r
    duparea*=4
    duparea+=find_intersection_area(0,0,(R-t-f), r+f)
    temp=0
    y=-g-2*r
    while True:
        if y-r <= -(R-t):
            break
        temp += find_intersection_area(0,y,(R-t-f), r + f)
        y-=g+2*r
    duparea+=temp*4
    return (totalArea-(sa - duparea))/ (pi * R * R)

def dist(a1,a2, b1, b2):
    return math.sqrt((a1-b1)**2 + (a2-b2)**2)

def pointDist(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def equals(a,b):
    return math.fabs(a-b)<0.000000001

def areaRect(point1, point2):
    return math.fabs(point1[0]-point2[0])*math.fabs(point1[1]-point2[1])

def trapArea(height, l2, l3):
    return height*(l2+l3)/2.0

def find_intersection_area(x, y, r, t):
    points = []
    points.append((x-t, y-t))
    points.append((x-t, y+t))
    points.append((x+t, y+t))
    points.append((x+t, y-t))
    intersectionsInside = []
    intersectionsOutside = []
    area=0
    for i in range(4):
        point = points[i]
        dist = math.sqrt(point[0] * point[0] + point[1] * point[1])
        if dist > r:
            intersectionsOutside.append(i)
        else:
            intersectionsInside.append(point)
    if intersectionsOutside:
        if len(intersectionsInside)==3:
            for i in intersectionsOutside:
                point1 = pointOnCircleX(points[i][0], r , points[i][1])
                point2 = pointOnCircleY(points[i][1], r, points[i][0])
                ax = areaBehindChord(point1, point2,r)
                for j in range(4):
                    if j==i:
                        continue
                    if not equals(points[j][0], point1[0]) and not equals(points[j][1], point1[1]) and not equals(points[j][0], point2[0]) and not equals(points[j][1], point2[1]):
                        diag=points[j]
                    if equals(points[j][0], point1[0]) or equals(points[j][1], point1[1]):
                        point1c=points[j]
                    if equals(points[j][0], point2[0]) or equals(points[j][1], point2[1]):
                        point2c=points[j]
                a1 = areaRect(diag, point1)
                d1 = pointDist(point1c, point1)
                d2 = pointDist(diag, point2c)-d1
                d3 = pointDist(point1c, diag)
                d4 = pointDist(point2c, point2)
                a2 = trapArea(d2, d3,d4);
                return a1+a2+ax
        elif len(intersectionsInside)==2:
            point1 = intersectionsInside[0]
            point2 = intersectionsInside[1]
            xsame = False
            if (math.fabs(point1[0] - point2[0]) < 0.0000000001):
                xsame=True
            maxDist=0
            if xsame:
                if math.fabs(point1[0]-(x+t))<0.000000001:
                    sign = x-t
                else:
                    sign = x+t
                point3 = pointOnCircleY(point1[1], r, sign)
                point4 = pointOnCircleY(point2[1], r, sign)
            else:
                if math.fabs(point1[1]-(y+t))<0.0000000001:
                    sign = y-t
                else:
                    sign = y+t
                point3 = pointOnCircleX(point1[0], r, sign)
                point4 = pointOnCircleX(point2[0], r, sign)
            ax = areaBehindChord(point3, point4,r)
            height = 2*t
            d1 = pointDist(point1, point3)
            d2 = pointDist(point2, point4)
            return ax + trapArea(height, d1, d2)
        elif len(intersectionsInside)==1:
            point = intersectionsInside[0]            
            if math.fabs(point[1]-(y+t)) < 0.00000001:
                sign = y-t
            else:
                sign = y+t
            point1 = pointOnCircleX(point[0], r, sign)
            if math.fabs(point[0]-(x+t)) < 0.00000001:
                sign = x-t
            else:
                sign = x+t
            point2 = pointOnCircleY(point[1], r, sign)
            dist1 = pointDist(point, point1)
            dist2 = pointDist(point, point2)
            ax = areaBehindChord(point1, point2,r)
            d1 = pointDist(point1, point)
            d2 = pointDist(point2, point)
            return ax + 0.5 * d1 * d2
        elif len(intersectionsInside)==0:
            a1 = stringArea(x,t,r)
            a2 = stringArea(y,t,r)
            if a1<a2:
                if x>0:
                    loc = x-t
                else:
                    loc = x+t
                if math.fabs(loc) < r:
                    point1=pointOnCircleX(loc, r, 1)
                    point2=pointOnCircleX(loc, r, -1)
                    if isBetween(point1[1], y-t, y+t) and isBetween(point2[1], y-t, y+t):
                        return a1
            else:
                if y>0:
                    loc = y-t
                else:
                    loc = y+t
                if math.fabs(loc) < r:
                    point1=pointOnCircleY(loc, r, 1)
                    point2=pointOnCircleY(loc, r, -1)
                    if isBetween(point1[0], x-t, x+t) and isBetween(point2[0], x-t, x+t):
                        return a2
 
            return 0
    elif intersectionsInside:
        area=4*t*t
    return area

def isBetween(x, a,b):
    if a>b:
        if x>b and x<a:
            return True
        else:
            return False
    else:
        if x>a and x<b:
            return True
        else:
            return False

def pointOnCircleX(x, r, sign):
    y = math.sqrt(r*r - x*x)
    if sign > 0:
        return (x,y)
    else:
        return (x,-y)

def pointOnCircleY(y, r, sign):
    x = math.sqrt(r*r - y*y)
    if sign > 0:
        return (x,y)
    else:
        return (-x,y)

def outsideArcArea(a, p,q,s,r):
    p=math.fabs(p)
    q=math.fabs(q)
    s=math.fabs(s)
    r=math.fabs(r)
    acos1 = math.acos(s/a)
    acos2 = math.acos(p/a)
    if acos2 > acos1:
        return outsideArcArea(a, s,r,p,q)
    area = 0.5 * (r * (s-p) + p * (q-r) + a*a*acos1 - a*a*acos2)
    return math.fabs(area)

def areaBehindChord(point1, point2, r):
    lenchord = pointDist(point1, point2)
    x = math.sqrt(r*r-lenchord*lenchord/4.0)
    theta = math.atan2(lenchord/2.0, x)
    a1=pi*r*r*(2*theta)/(2*pi)-(lenchord/2.0)*x
    a2 = pi*r*r - a1
    if a1>a2:
        return a2
    else:
        return a1

def stringArea(x, r, a):
    x = math.fabs(x)
    if (math.fabs(x-r)>=a):
        return pi * a*a
    l1 = math.sqrt(a**2-((x-r)**2))
    theta = math.atan2(l1,math.fabs((x-r)));
    a1 = pi*a*a-(((2*pi-2*theta)/(2*pi))*pi*a*a+l1*math.fabs(x-r))
    if (x+r)>=a:
        return a1;
    else:
        l2 = math.sqrt(a**2-((x+r)**2))
        phi = math.atan2(l2,math.fabs(x+r));
        a2 = pi*a*a-(((2*pi-2*phi)/(2*pi))*pi*a*a+l2*math.fabs(x+r))
    if ((x-r) * (x+r) < 0):
        return pi * a*a - (a1+a2)
    return math.fabs(a1-a2)

ninputs= int(sys.stdin.readline())
for i in range(ninputs):
    line = sys.stdin.readline()
    tokens=line.split()
    f= float(tokens[0])
    R = float(tokens[1])
    t = float(tokens[2])
    r = float(tokens[3])
    g = float(tokens[4])
    p = probability(t,f,g,r,R)
    print "Case #%d: %.9f" %((i+1), 1.0-p)

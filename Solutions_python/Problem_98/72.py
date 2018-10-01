# -*- coding:utf-8 -*-
import os, math, cmath
from itertools import product
basepath = '/Users/voidus/Documents/workspace/xp/jam/files/mirrors'

srcfilename = os.path.join(basepath, 'D-small-attempt1.in')
dstfilename = os.path.join(basepath, 'D-small-attempt1.out.txt')

#srcfilename = os.path.join(basepath, 'sample1.in')
#dstfilename = os.path.join(basepath, 'sample1.out.txt')


def solve(width, height, x, y, depth):
    angles = []
#    goodpoints = []
    result = 0
    x = x+0.5
    y = y+0.5
    dopx = abs(width-x)
    dopy = abs(height-y)
    if 2*x <= depth:
        result += 1
    if 2*y <= depth:
        result += 1
    if 2*dopx <= depth:
        result += 1
    if 2*dopy <= depth:
        result += 1
    boundk = depth//(2*width)+1
    boundl = depth//(2*height)+1
    for i in xrange(-boundk, boundk+1):
        for j in xrange(-boundl, boundl+1):
            xs = [2*width*i, 2*width*i-2*x]
            ys = [2*height*j, 2*height*j+2*y]
            if i == 0:
                del xs[0]
            if j == 0:
                del ys[0]
            points = [complex(re,im) for re, im in product(xs, ys)]
            for point in points:
                if abs(point) <= depth:
                    phase = cmath.phase(point)
                    dup = False
                    for angle in angles:
                        if abs(phase-angle) <= 0.000001:
                            dup = True
                    if not dup:
                        result += 1
                        angles.append(phase)
                        angles.sort()
#                        goodpoints.append(point)
#    print '='*20
#    for goodpoint in goodpoints:
#        print goodpoint
#    print '='*20
    return result

if __name__ == '__main__':
    with open(srcfilename, 'rb') as inp:
        with open(dstfilename, 'wb') as outp:
            lines = inp.readlines()
            count = int(lines.pop(0))
            outlines = []
            j = 0
            for i in xrange(count):
                x = y = -1
                height, width, depth = [int(digit) for digit in lines[j].split()]
                for linecount in xrange(0, height):
                    j += 1
                    if 'X' in lines[j]:
                        y = linecount-1
                        x = lines[j].index('X')-1
                result = solve(width-2, height-2, x, y, depth)
                outlines.append('Case #%d: %d\n' % (i+1, result))
                j += 1
            outp.writelines(outlines)

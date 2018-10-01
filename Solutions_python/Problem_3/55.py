#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Scott Patterson
# asp742@gmail.com
#

import sys
import math

def area_circ_seg(c, d, r):
    return r*r*math.asin((.5/r)*c) - .5*c*d

def area_partial_gap(inner_radius, fly_radius, gap_width, x, y):
    x += fly_radius
    y += fly_radius

    usable_radius = inner_radius - fly_radius
    usable_radius_2 = usable_radius**2

    arc_a = [0.,0.]
    arc_b = [0.,0.]

    if in_circle(x + gap_width - 2*fly_radius, y, usable_radius_2):
        arc_a[0] = x + gap_width - 2*fly_radius
        arc_a[1] = math.sqrt(usable_radius_2 - arc_a[0]**2)
    else:
        arc_a[1] = y
        arc_a[0] = math.sqrt(usable_radius_2 - arc_a[1]**2)

    if in_circle(x, y + gap_width - 2*fly_radius, usable_radius_2):
        arc_b[1] = y + gap_width - 2*fly_radius
        arc_b[0] = math.sqrt(usable_radius_2 - arc_b[1]**2)
    else:
        arc_b[0] = x
        arc_b[1] = math.sqrt(usable_radius_2 - arc_b[0]**2)

    c_2 = dist_2(arc_a, arc_b)
    c = math.sqrt(c_2)
    d = math.sqrt(usable_radius_2 - (.25*c_2))
    h = usable_radius - d

    circ_area = area_circ_seg(c, d, usable_radius)

    tri_area  = (arc_b[0] - x) * (arc_b[1] - y)
    tri_area += .5 * (arc_a[0] - arc_b[0]) * (arc_a[1] + arc_b[1] - 2*y)

    return tri_area + circ_area

def dist_2(a, b):
    return sum((b_i - a_i)**2 for a_i, b_i in zip(a,b))

def in_circle(x, y, radius_2):
    return dist_2((0.0, 0.0), (x, y)) < radius_2

def gap_generator(radius, width, gap, fly_radius):
    x = y = width

    radius_2 = radius**2
    step = gap + 2*width

    while in_circle(0, y, radius_2):
        while in_circle(x, 0, radius_2):
            if in_circle(x+fly_radius, y+fly_radius, radius_2):
                yield (x,y)
            x += step
        x = width
        y += step

def get_prob(fly_radius, radius, thickness, width, gap_width):

    # normalize to radius = 1.0
    one_radius  = 1./radius
    radius      = 1.0
    fly_radius *= one_radius
    thickness  *= one_radius
    width      *= one_radius
    gap_width  *= one_radius
    
    inner_radius = radius - thickness
    inner_radius_2 = inner_radius**2

    escapable_gap = (gap_width - 2*fly_radius)**2
    escapable_gap = escapable_gap if escapable_gap > 0.0 else 0.0

    escapable_sum = 0.0

    for x, y in gap_generator(inner_radius - fly_radius, width,
            gap_width, fly_radius):
        if in_circle(x+gap_width, y+gap_width, inner_radius_2):
            escapable_sum += escapable_gap
        else:
            escapable_sum += area_partial_gap(inner_radius, fly_radius,
                                              gap_width, x, y)


    return 1. - (4./math.pi)*escapable_sum

def main():
    file = sys.argv[1]
    data = (lines.strip() for lines in open(file))

    ncase = int(data.next())

    params = ([float(x) for x in d.split()] for d in data)

    fly_prob = (get_prob(*p) for p in params)

    for case in range(ncase):
        print 'Case #%d: %.6f' % (case+1, fly_prob.next())

if __name__ == '__main__':
    main()

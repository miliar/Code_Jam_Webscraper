#! /usr/bin/env python

# google codejam: Fly Swatter
# Fuchang Yin <fuchangyin@gmail.com>
# Thu Jul 17 16:24:13 EDT 2008

from math import *
DRAW_GEOM = False
#DRAW_GEOM = True

def squar_space( par, case_i=0 ):
    f, R, t, r, g = par
    sql = g - f - f
    Rin = R - t - f
    Rin2 = Rin*Rin
    if sql < 0:
        sqspace = 0
        return sqspace
    if DRAW_GEOM:
        jgeom_lines = []
        gsqures = get_all_squares( [0,R,t,r,g] )
        g_lines = square_draw_lines( gsqures )
        geom_lines = g_lines
    # through areas
    squares = get_all_squares( par )
    areas = []
    for sqr in squares:
        poss = am_i_in_r( par, sqr )
        xmin, ymin, xmax, ymax = sqr
        if poss[0] == False:
            myarea = 0
        elif poss[3] == True:
            myarea = sql*sql
        elif poss[2] == False and poss[1] == True:
            intg = ( (Rin2-xmax*xmax)**0.5*xmax - (Rin2-xmin*xmin)**0.5*xmin + \
                     Rin2*( asin(xmax/Rin) - asin(xmin/Rin) ) ) / 2
            sub = ( xmax - xmin ) * ymin
            myarea = intg - sub
        elif poss[2] == True and poss[1] == True:
            x1 = ( Rin2 - ymax*ymax )**0.5
            y1 = ( Rin2 - xmax*xmax )**0.5
            intg = ( (Rin2-xmax*xmax)**0.5*xmax - (Rin2-x1*x1)**0.5*x1 + \
                     Rin2*( asin(xmax/Rin) - asin(x1/Rin) ) ) / 2
            sub = ( xmax - x1 ) * ymin
            are = intg - sub
            myarea = are + sql*(x1-xmin)
        elif poss[2] == True and poss[1] == False:
            intg = ( (Rin2-ymax*ymax)**0.5*ymax - (Rin2-ymin*ymin)**0.5*ymin + \
                     Rin2*( asin(ymax/Rin) - asin(ymin/Rin) ) ) / 2
            sub = ( ymax - ymin ) * xmin
            myarea = intg - sub
        elif poss[2] == False and poss[1] == False:
            x2 = ( Rin2 - ymin*ymin )**0.5
            y2 = ( Rin2 - xmin*xmin )**0.5
            intg = ( (Rin2-x2*x2)**0.5*x2 - (Rin2-xmin*xmin)**0.5*xmin + \
                     Rin2*( asin(x2/Rin) - asin(xmin/Rin) ) ) / 2
            sub = ( x2 - xmin ) * ymin
            myarea = intg - sub
        else:
            print poss
            raise
        areas.append( myarea )
        # get square inside Rin
        if DRAW_GEOM:
            if poss[0] == True or True:
                geom_lines.append( "%8.3f %8.3f\n" % (sqr[0],sqr[1]) )
                geom_lines.append( "%8.3f %8.3f\n" % (sqr[2],sqr[1]) )
                geom_lines.append( "%8.3f %8.3f\n" % (sqr[2],sqr[3]) )
                geom_lines.append( "%8.3f %8.3f\n" % (sqr[0],sqr[3]) )
                geom_lines.append( "%8.3f %8.3f\n" % (sqr[0],sqr[1]) )
                geom_lines.append( "\n" )
    if DRAW_GEOM:
        nstep = 500
        radius = R
        r2 = radius*radius; x = 0; step = radius/nstep
        for i in range( nstep ):
            y = (r2 - x*x)**0.5
            geom_lines.append( "%10.6f %10.6f\n" % ( x,y ) )
            x = x + step
        geom_lines.append( "%10.6f %10.6f\n" % ( radius, 0 ) )
        geom_lines.append( "\n" )
        radius = Rin
        r2 = radius*radius; x = 0; step = radius/nstep
        for i in range( nstep ):
            y = (r2 - x*x)**0.5
            geom_lines.append( "%10.6f %10.6f\n" % ( x,y ) )
            x = x + step
        geom_lines.append( "%10.6f %10.6f\n" % ( radius, 0 ) )
        geom_lines.append( "\n" )
        fname = "geom_%i.dat" % case_i
        f = file( fname, "w" )
        f.writelines( geom_lines )
        f.close()
    sum_areas = sum( areas )
    return sum_areas

def square_draw_lines( squares ):
    lines = []
    for sqr in squares:
        lines.append( "%8.3f %8.3f\n" % ( sqr[0],sqr[1] ) )
        lines.append( "%8.3f %8.3f\n" % ( sqr[2],sqr[1] ) )
        lines.append( "%8.3f %8.3f\n" % ( sqr[2],sqr[3] ) )
        lines.append( "%8.3f %8.3f\n" % ( sqr[0],sqr[3] ) )
        lines.append( "%8.3f %8.3f\n" % ( sqr[0],sqr[1] ) )
        lines.append( "\n" )
    return lines

def am_i_in_r( par, sqr ):
    f, R, t, r, g = par
    Rin = R - t - f
    p1 = [ sqr[0], sqr[1] ]
    p2 = [ sqr[2], sqr[1] ]
    p3 = [ sqr[0], sqr[3] ]
    p4 = [ sqr[2], sqr[3] ]
    ds = [ a*a+b*b for a,b in [p1,p2,p3,p4] ]
    Rin2 = Rin*Rin
    inr = [ e<Rin2 for e in ds ]
    return inr

def get_all_squares( par ):
    f, R, t, r, g = par
    rf = f + r
    Rin = R - t - f
    sql = g - f - f
    shift = g + r + r
    #print "square length = %.6f" % sql
    #print "shift = %.6f" % shift
    # current lower left
    xmin = rf
    ymin = rf
    count = 0
    row = []
    while True:
        xmax = xmin + sql
        ymax = ymin + sql
        sqr = [ xmin, ymin, xmax, ymax ]
        row.append( sqr )
        xmin = xmin + shift
        xmax = xmax + shift
        count = count + 1
        if xmin > Rin:
            break
    squares = []    # contain squares of [ [xmin,ymin,xmax,ymax], ... ]
    dy = 0
    for i in range( 1, count ):
        dy = dy + shift
        newrow = []
        for sqr in row:
            xmin,ymin,xmax,ymax = sqr
            newsqure = [ xmin, ymin+dy, xmax, ymax+dy ]
            newrow.append( newsqure )
        squares.extend( newrow )
    squares = row + squares
    return squares

def main():
    import sys
    argv = sys.argv
    fin = argv[1]
    f = file( fin )
    ls = f.readlines()
    f.close()
    nc = int( ls[0] )
    for i in range( 1, nc+1 ):
        line = ls[i]
        par = [ float(e) for e in line.split() ]
        f, R, t, r, g = par
        Rin = R - t - f
        square_area = squar_space( par, i )
        Scircle = pi*R*R
        qcircle = Scircle/4
        ratio = square_area / qcircle
        prob = 1 - ratio
        #print "f=%.6f, R=%.6f, t=%.6f, r=%.6f, g=%.6f" % tuple(par)
        #print "squares = %.6f" % square_area
        #print "Scircle = %.6f, Scircle/4 = %.6f" %(Scircle,Scircle/4 )
        #print "ratio = %.6f" % ratio
        print "Case #%i: %.6f" %( i, prob )
    return

if __name__ == "__main__":
    main()


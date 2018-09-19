def mprint(a):
    print (a)

def lprint(bool,a):
    if bool:
        print a

class Config:

    def set_vars(self,h,w,xpos,ypos,d):
        self.h = h-2
        self.w = w-2
        self.d = d
        self.xpos = xpos
        self.ypos = ypos

    def __init__(self,f):
        line = f.readline()
        fields = line.split()
        h = int(fields.pop(0))
        w = int(fields.pop(0))
        d = int(fields.pop(0))
        x_pos = 0
        y_pos = 0
        for i in xrange(h):
            line = f.readline()
            for j in xrange(w):
                #lprint(True,"line " + line)
                if (line[j] == "X"):
                    lprint(True,"Found X")
                    x_pos = j-.5
                    y_pos = i-.5
        self.set_vars(h,w,x_pos,y_pos,d)


    def display(self):
        mprint (str(config.h) + " " + str(config.w) + " " + str(config.d))
        line = ""
        for j in xrange(self.w+2):
            line += "#"
        mprint(line)
        for i in xrange(self.h):
            line = "#"
            for j in xrange(self.w):
                if (self.ypos==i+.5 and self.xpos == j+.5):
                    line += "X"
                else:
                    line += "."
            line+="#"
            mprint(line)
        line = ""
        for j in xrange(self.w+2):
            line += "#"
        mprint(line)
        print "xpos/ypos", self.xpos, self.ypos


def find_reflected_X(config,i,j):
    do_print = False
    corner_x = i*(config.w)
    corner_y = j*(config.h)
    if (i%2 == 0):
        X_pos = corner_x + config.xpos
    else:
        X_pos = corner_x - config.xpos + config.w
    if (j%2 == 0):
        Y_pos = corner_y + config.ypos
    else:
        Y_pos = corner_y - config.ypos + config.h

    lprint (do_print,"config.x " + str(config.xpos) + " config.y " + str (config.ypos))
    lprint (do_print,"i " + str(i) + " j " + str (j))
    lprint (do_print,"X_POS " + str(X_pos) + " Y_POS " + str (Y_pos))
    return[X_pos,Y_pos]

#f = open("mirror.test","r")
#f = open("small-mirror.test","r")
f = open("D-small-attempt2.in","r")

s = f.readline()
ntrials = int(s)

i =0

fout = open("mirror.out","w")

def square(x):
    return x*x

def dist2(p1,p2):
    return (((square(p1[0] - p2[0])) + square(p1[1] - p2[1])))

def distP(p1,p2,d):
    do_print = False
    lprint(do_print, str(p1)+str(p2) + " " + str(d))
    return ( dist2(p1,p2) <= d*d)

def slope(p1,p2):
    return (p1[1]-p2[1])/(p1[0]-p2[0])

def same_side(p,p1,p2,index):
    return ((p[index]-p1[index])*(p[index]-p2[index]) >=0)

def slopes(p,points):
    result = []
    for p1 in points:
        if (p1[0] != p[0]):
            result.append([p1,slope(p1,p)])
        else:
            result.append([p1,"vertical"])
    return result

def mykey(elt):
    return elt[1]

def new_eliminate_intersections(p,points):
    doprint = False
    point_slopes = slopes(p,points)
    point_slopes.sort(key=mykey)
    lprint (doprint,"pointslopes!!!" + str(point_slopes))
    eliminated = []
    for i in xrange(len(point_slopes)):
        p1 = point_slopes[i][0]
        try:
            eliminated.index(p1)
        except:
            for j in xrange(i+1,len(point_slopes)):
                if (point_slopes[i][1] != point_slopes[j][1]):
                    lprint(doprint,"breaking " + str(i) + "-- i and j is -- " + str(j))
                    break
                p2 = point_slopes[j][0]
                try:
                    eliminated.index(p2)
                except:
                    if (((p[0] == p2[0]) and (p[0] == p1[0]) and same_side(p,p1,p2,1)) or
                        ((p[0] != p2[0]) and (p[0] != p1[0]) and
                         slope(p,p1) == slope(p,p2) 
                         and same_side(p,p1,p2,0))):
                        if (dist2(p,p1) <= dist2(p,p2)):
                            eliminated.append(p2)
                            lprint(doprint, "elimating p2 " + str(p2) + " due " 
                                   + str(p1) + " and center " + str(p) )
                        else:
                            eliminated.append(p1)
                            lprint(doprint, "elimating p1" + str(p1) + " due " 
                                   + str(p2) + " and center " + str(p) )
                            break
                    else:
                        lprint(doprint, "not elimating " + str(p1) + " due " 
                               + str(p2) + " and center " + str(p) )
              
    lprint(doprint, "point_slope: elimating " + str(eliminated) + " for center " + str(p))
    for e in eliminated:
        points.remove(e)
    return points
                
    

def eliminate_intersections(p,points):
    doprint = False
    eliminated = []
    lprint (doprint,"points!!!" +str(points))
    for i in xrange(len(points)):
        p1 = points[i]
        try:
            eliminated.index(p1)
        except:
            for j in xrange(i+1,len(points)):
                #print i, j, "!!!!"
                p2 = points[j]
                try:
                    eliminated.index(p2)
                except:
                    if (((p[0] == p2[0]) and (p[0] == p1[0]) and same_side(p,p1,p2,1)) or
                        ((p[0] != p2[0]) and (p[0] != p1[0]) and
                         slope(p,p1) == slope(p,p2) 
                         and same_side(p,p1,p2,0))):
                        if (dist2(p,p1) <= dist2(p,p2)):
                            eliminated.append(p2)
                            lprint(doprint, "elimating p2 " + str(p2) + " due " 
                                   + str(p1) + " and center " + str(p) )
                        else:
                            eliminated.append(p1)
                            lprint(doprint, "elimating p1" + str(p1) + " due " 
                                   + str(p2) + " and center " + str(p) )
                            break
                    else:
                        lprint(doprint, "not elimating " + str(p1) + " due " 
                               + str(p2) + " and center " + str(p) )
              
    lprint(True, "orig:elimating " + str(eliminated) + " for center " + str(p))
    for e in eliminated:
        points.remove(e)
    return points
        
    
def verify_points(p,points,d):
    for e in points:
        if (dist2(p,e) > d*d):
            print "Failure"

for trial in xrange(ntrials):
    # should put in config class...
    config = Config(f)
    #config = Config(w.h,x_pos,y_pos,d)
    config.display()
    result = []
    ilim = config.d/config.w+2
    print "h,w,d ---", config.h,config.w,config.d
    print "ilim --", ilim
    jlim = config.d/config.h+2
    print "jlim --", jlim
    for i in xrange(-ilim,ilim):
        for j in xrange(-jlim,jlim):
            if (i == 0 and j ==0):
                continue
            new_pos = find_reflected_X(config,i,j)
            if distP([config.xpos,config.ypos],new_pos,config.d):
                result.append(new_pos)

    #print "Resulting points ", result
    verify_points([config.xpos,config.ypos],result,config.d)
    result = new_eliminate_intersections([config.xpos,config.ypos],result[:])
    #result = eliminate_intersections([config.xpos,config.ypos],result)

    #if (len(result1) != len(result)):
    #    print "Uh oh"
            
    #result = "NOTHING YET"
    #print "Resulting points ", result
    verify_points([config.xpos,config.ypos],result,config.d)

    print "Case #" + str(trial+1) + ": "  + str(len(result))
    fout.write("Case #" + str(trial+1) + ": "  + str(len(result)) +"\n")



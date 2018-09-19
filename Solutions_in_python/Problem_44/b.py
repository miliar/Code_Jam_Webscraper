import math
import random
import re

if __name__ == '__main__':
    #in_filename = "B-small.in"
    #in_filename = "B-dummy.in"
    in_filename = "B-large.in"
    #out_filename = "B-small.out"
    out_filename = "B-large.out"
    
    in_file = open(in_filename, 'r')
    out_file = open(out_filename, 'w')

    num_cases  = int(in_file.readline())
    for c in range(0,num_cases):
        num = int(in_file.readline())
        cx = cy = cz = 0.0
        vx = vy = vz = 0.0
        for n in range(num):
            tcx, tcy, tcz, tvx, tvy, tvz = [float(x) for x in in_file.readline().split()]
            cx = cx + tcx
            cy = cy + tcy
            cz = cz + tcz
            vx = vx + tvx
            vy = vy + tvy
            vz = vz + tvz
        print vx**2 + vy**2 + vz**2 
        if(vx**2 + vy**2 + vz**2 == 0):
            print "!!!",(c+1),vx,vy,vz
            t = 0
        else:
            t = (-2.0)*(vx*cx + vy*cy + vz*cz)/(2.0*(vx**2 + vy**2 + vz**2)) 
        if t < 0:
            t = 0
        #intd = (vx**2 + vy**2 + vz**2)*t**2 + 2.0*t*(vx*cx + vy*cy + vz*cz) + (cx**2 + cy**2 + cz**2)
        #intd = math.sqrt(intd)
        intd = math.sqrt(((vx*t + cx)/num)**2 + ((vz*t + cz)/num)**2 + ((vy*t + cy)/num)**2) 
        #print (c+1),t,intd
        b = (-2.0)*(vx*cx + vy*cy + vz*cz)
        a = (vx**2 + vy**2 + vz**2)
        out_file.write("Case #%d: %f %f\n" % (c+1, intd, t))

    out_file.close()


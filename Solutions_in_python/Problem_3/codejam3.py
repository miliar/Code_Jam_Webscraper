
from math import *
s = '''5
0.25 1.0 0.1 0.01 0.5
0.25 1.0 0.1 0.01 0.9
0.00001 10000 0.00001 0.00001 1000
0.4 10000 0.00001 0.00001 700
1 100 1 1 10'''
import tools


def distance(p1, p2):
    return sqrt((p1[1] - p2[1])**2 + (p1[0] - p2[0])**2)

def point_in_circle(point, radius):
#    print point
    return distance(point, [0, 0]) <= radius

count = 0
for line in s.split("\n")[1:]:
    count += 1
    f, R, t, r, g = map(float, line.split(' '))

    #apply fly radius
    
    r += f
    t += f
    g -= 2*f
    
    total_area = (pi * R**2)/4
    inner_circle = R-t
    #add full squares
    area = 0.0
    max_blocks_x = int((inner_circle)/(g+r*2)) + 10

    for x in range(0, max_blocks_x ):
        for y in range(0, max_blocks_x ):
            #complete square inside
            if  point_in_circle([r + x * (g + 2*r) +g, r + y * (g + 2*r) + g], inner_circle):
                area += g**2
            else:
                if point_in_circle([r + (x) * (g + 2*r), r + (y) * (g + 2*r)], inner_circle): #bottom left point in circle
                    #top left, bottom right both outside
                    if (not point_in_circle([r + (x) * (g + 2*r), r + (y) * (g + 2*r) + g], inner_circle)) and (not point_in_circle([r + (x) * (g + 2*r) + g, r + (y) * (g + 2*r)], inner_circle)): 
                        
                        x1 = r + (x) * (g + 2*r)
                        y1 = sqrt(inner_circle**2 - x1**2)
                        
                        y2 = r + (y) * (g + 2*r)
                        x2 = sqrt(inner_circle**2 - y2**2)
                        theta = tools.angle_between(complex(x1,y1), complex(x2,y2))

                        slice_r = (theta * inner_circle)

                        slice = (pi * inner_circle**2)*  theta/ (2 * pi)
                        triangle = 0.5 * distance([x1,y1], [x2, y2]) * sqrt( inner_circle**2 - (distance([x1,y1], [x2, y2])/2)**2 )

                        area += slice - triangle
                        
                        area += abs((x2-x1)*(y2-y1))*0.5

                        
                    #top left, bottom right both inside                        
                    elif (point_in_circle([r + (x) * (g + 2*r), r + (y) * (g + 2*r)+g], inner_circle)) and (point_in_circle([r + (x) * (g + 2*r) +g, r + (y) * (g + 2*r)], inner_circle)):                         
                        
                        x1 = r + (x) * (g + 2*r) +g
                        y1 = sqrt(inner_circle**2 - x1**2)
                        
                        y2 = r + (y) * (g + 2*r) +g
                        x2 = sqrt(inner_circle**2 - y2**2)
                        theta = tools.angle_between(complex(x1,y1), complex(x2,y2))

                        slice_r = (theta * inner_circle)

                        slice = (pi * inner_circle**2)*  theta/ (2 * pi)
                        triangle = 0.5 * distance([x1,y1], [x2, y2]) * sqrt( inner_circle**2 - (distance([x1,y1], [x2, y2])/2)**2 )

                        area += slice - triangle
                        
                        area += abs((x2-x1)*(y2-y1))*0.5
                        
                        area += abs((x2 - (r + (x) * (g + 2*r))) * ( (r + (y) * (g + 2*r)+g) - (r + (y) * (g + 2*r))))
                        
                        
                        area += abs((y1 - (r + (y) * (g + 2*r))) * ( (r + (x) * (g + 2*r)+g) - x2))
                        
            
                    #top left inside, bottom right outside
                    elif (point_in_circle([r + (x) * (g + 2*r), r + (y) * (g + 2*r)+g], inner_circle)) and (not point_in_circle([r + (x) * (g + 2*r)+g, r + (y) * (g + 2*r)], inner_circle)):                         
                        
                       
                        y1 = r + (y) * (g + 2*r)
                        x1 = sqrt(inner_circle**2 - y1**2)
                        
                        y2 = r + (y) * (g + 2*r)+g
                        x2 = sqrt(inner_circle**2 - y2**2)                        
                        theta = tools.angle_between(complex(x1,y1), complex(x2,y2))


                        slice_r = (theta * inner_circle)

                        slice = (pi * inner_circle**2)*  theta/ (2 * pi)
                        triangle = 0.5 * distance([x1,y1], [x2, y2]) * sqrt( inner_circle**2 - (distance([x1,y1], [x2, y2])/2)**2 )

                        area += 2*(slice - triangle)
                        
                        area += 2*abs((x2-x1)*(y2-y1))*0.5
                        
                        area += 2*abs((x2 - (r + (x) * (g + 2*r))) * ( (r + (y) * (g + 2*r)+g) - (r + (y) * (g + 2*r))))
                        

    print 'Case #%i: %0.6f' %(count, 1 - area / total_area)
    





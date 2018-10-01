from math import *

def parseInput(fileName): # Parses the input
  h = open(fileName)
  n = int(h.readline())
  res = [] # Array of parsed input
  for i in range(0, n):
    line = h.readline()
    line = line[0:len(line)-1]
    res.append(map(lambda x: float(x), line.split(" ")))
  # Close file and return result
  h.close()
  return res

def triangleArea(x0, y0, x1, y1, x2, y2):
  a = sqrt( (x1-x0)**2 + (y1-y0)**2 )
  b = sqrt( (x2-x0)**2 + (y2-y0)**2 )
  ab = (x1-x0)*(x2-x0) + (y1-y0)*(y2-y0)
  if a == 0 or b == 0:
    return 0
  return 0.5*b*a*sqrt(1 - (ab/(a*b))**2)

def fullArea(f, R, t, r, g): # Returns the area in which the center point can
                             # occur for a full square
  return (g-2*f)**2 if g-2*f > 0 else 0

def partialArea(f, R, t, r, g, v, w): # Returns the area in which the center
                                      # point can occur for a non-complete
                                      # square. The function assumes x and y
                                      # are in the first quadrant.
  # The final area
  A = 0
  # Find effective coordinates of the area to be calculated
  x = v + r + f
  y = w + r + f
  a = R - t - f
  # If the adjust coordinates are out, leave
  if (x**2 + y**2) >= a**2:
    return 0
  # Find the point at which the horizontal line crosses the circle
  xh = sqrt(a**2 - y**2)
  # Find the point at which the vertical line crosses the circle
  yv = sqrt(a**2 - x**2)
  # Leave if there is no area
  if xh <= x or yv <= y:
    return 0
  # Don't include multiple squares (Notice it can't happen horizontally and
  # vertically at the same time, since it would include a full square
  if xh > x + (g-2*f) and yv > y + (g-2*f):
    xh = x + (g-2*f)
    yv = y + (g-2*f)
    xn = sqrt(a**2 - yv**2)
    yn = sqrt(a**2 - xh**2)
    A += (xh-x)*(yn-y)
    A += (xn-x)*(yv-yn)
    x = xn
    y = yn
  if xh > x + (g-2*f):
    xh = x + (g-2*f)
    yn = sqrt(a**2 - xh**2)
    A += (xh-x)*(yn-y)
    y = yn
  if yv > y + (g-2*f):
    yv = y + (g-2*f)
    xn = sqrt(a**2 - yv**2)
    A += (xn-x)*(yv-y)
    x = xn
  # Find the angle covered by the arc
  theta1 = atan(y/xh) if xh != 0 else pi/2
  theta2 = atan(yv/x) if x != 0 else pi/2
  theta = theta2 - theta1
  # Find the area of the setor
  A += (a**2) * theta / 2
  # Subtract the area of the two triangles, leaving the area in question
  A -= triangleArea(0,0, x,y, xh, y)
  A -= triangleArea(0,0, x,y, x, yv)
  # Return the area
  return A

def solve(f, R, t, r, g):
  res = 0;
  for i in range(0, int(ceil((R-t)/(g+2*r))) + 1):
    for u in range(0, i + 1):
      x = i * (g+2*r)
      y = u * (g+2*r)
      if (x**2 + y**2) >= (R-t)**2: # Make sure you are still inside the ring
        continue
      if ((x+g+2*r)**2 + (y+g+2*r)**2) <= (R-t)**2:
        # Square is completely inside the ring
        res += fullArea(f, R, t, r, g)/(1 if i != u else 2)
      else:
        # Square is partially inside the ring
        res += partialArea(f, R, t, r, g, x, y)/(1 if i != u else 2)
  res = 1 - (res / (pi * (R**2) / 8))
  res = res * 10**7
  res = float(int(res))/10**7
  return res

x = parseInput("C-small-attempt0.in") # Parse the input
outputs = ""
for i in range(0, len(x)): # Loop over all cases
  outputs += "Case #" + str(i+1) + ": " + str(solve(x[i][0], x[i][1], x[i][2], x[i][3], x[i][4])) + "\n"
# Write output to file
h = open("prob-C.out", "w")
h.write(outputs)
h.close()

import math

fileName = "A-large.in"
f = open(fileName, 'r')

outputName = "A-large-out.txt"
output = open(outputName, 'w')

line = f.readline()
T = int(line)

for t in range(T):
    res = ""
    line = f.readline()
    line = line.split()
    N = int(line[0])
    K = int(line[1])

    areas = []
    for i in range(N):
        line = f.readline()
        R, H = map(int, line.split())
        topArea = math.pi * (R**2)
        sideArea = H * R * 2 * math.pi
        areas.append([topArea, sideArea])
    
    areas.sort(key=lambda tup: tup[0], reverse = True)
    
    maxArea = 0
    for i in range(N - K + 1):
        area = areas[i][0]
        area += areas[i][1]
        tower = areas[i + 1:]
        tower.sort(key=lambda tup: tup[1], reverse = True)
        for j in range(K - 1):
            area += tower[j][1]
        maxArea = max(maxArea, area)
        
    res = "{0:.9f}".format(maxArea)
        
    print("Case #{}: {}".format(t+1, res))
    output.write("Case #{}: {}".format(t+1, res))
    output.write("\n")
    
output.close()
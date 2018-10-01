import math

def sumn(p):
    return p * (p + 1) / 2

def recycles(A, B):
    result = 0
    if B < 10:
        result = 0
    else:
        numsdone = {}
        for i in range(A, B + 1):
            xresults = 0
            x = str(i)
            if x not in numsdone:
                perms = []
                for i in range(1, len(x)):
                    rstring = x[i:] + x[0:i]
                    recycle = int(rstring)
                    if x != rstring and rstring not in perms and recycle >= A and recycle <= B:
                        perms.append(rstring)
                        numsdone[rstring] = True
                        xresults += 1
            xresults += sumn(xresults - 1)
            result += xresults
    return result

input = open('C:\\Users\\Adam\\Downloads\\CodeJam\\C-large.in', 'r')
output = open('C:\\Users\\Adam\\Downloads\\CodeJam\\outputs.out', 'w')
cases = int(input.readline())
thiscase = 1
    
while thiscase <= cases:
    limits = input.readline().split(' ')
    A, B = int(limits[0]), int(limits[1])
    output.write('Case #' + str(thiscase) + ': ' + str(recycles(A, B)) + '\n')
    thiscase += 1
    
input.close()
output.close()



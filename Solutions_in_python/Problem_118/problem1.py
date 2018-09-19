import math

def ispalindrom(numb):
    numb = str(numb)
    length = len(numb)
    if length == 1:
        return True
    elif length%2 != 0:
        start = 0
        end = length - 1
        while length != 1:
            if not numb[start] == numb[end]:
                break
            else:
                length = length - 2
                start = start + 1
                end = end - 1
                if length == 1:
                    return True
    elif length%2 == 0:
        start = 0
        end = length - 1
        while length != 0:
            if not numb[start] == numb[end]:
                break
            else:
                length = length - 2
                start = start + 1
                end = end - 1
                if length == 0:
                    return True
            
            
fname = 'C-small-attempt1.in'
with open(fname) as f:
    content = f.readlines()
inputs = int(content[0])
input_count = 1
for i in range(1, len(content)):
    count = 0
    endpoints = content[input_count].split(' ')
    start_point = int(endpoints[0])
    end_point = int(endpoints[1])
    for i in range(start_point, end_point+1):
        if ispalindrom(i):
            sqroot = math.sqrt(i)
            if sqroot%1 == 0:
                sqroot = '%.12g' % sqroot
                sqroot = int(sqroot)
                if ispalindrom(sqroot):
                    count = count + 1
            else:
                pass
    f = open('result.txt', 'a')
    f.write('Case #'+str(input_count)+': '+str(count)+'\n')
    f.close()
    input_count += 1

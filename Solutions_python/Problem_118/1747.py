from math import sqrt, ceil, floor

def check_case(a, b):
    matches = 0
    for i in range(int(ceil(sqrt(a))), int(floor(sqrt(b))) + 1):
        if is_pal(i) and is_pal(i*i):
            matches += 1
    return matches

def is_pal(i):
    a = str(i)
    b = a[::-1]
    if a == b:
        return True
    return False
    
file = open("input.txt", "r")
num_cases = file.readline()
count = 1
for line in file:
    a, b = line.split()
    a = int(a)
    b = int(b)
    print "Case #%d: %s" %(count, check_case(a, b))
    count += 1
    

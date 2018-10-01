
from math import ceil, sqrt


def is_fair(number):
    chars = [char for char in str(number)]

    start = 0
    end = len(chars) - 1
    
    fair = True
    while start < end:
        if chars[start] != chars[end]:
            fair = False
            break

        start += 1
        end -= 1

    return fair



fin = open("c.in")

cases = int(fin.readline().strip())

for c in range(cases):
    line = fin.readline().strip().split(" ")
    lower, upper = int(line[0]), int(line[1])

    numbers = 0
    i = long(ceil(sqrt(lower)))

    while True:
        sqr = i * i

        if sqr > upper:
            break
 
        if is_fair(i) and is_fair(sqr):
            numbers += 1

        i += 1

    print "Case #%d: %d" % (c + 1, numbers)

fin.close()

import sys

def cel(a, b):
    #print '%s %s'%(a, b)
    output = list()
    aa = int(a)
    bb = int(b)
    count = 0
    for num in range(1, len(str(a))):
        for number in range(aa, bb+1):
            w = int('%s%s'%(str(number)[num:], str(number)[:num]))
            #print '%s >> %s'%(number, w)
            if number >= aa and w <= bb and number < w :
                #print ' * '
                #if not w in output:
                count += 1
                #output.append(w)
    return count

i = 0
for line in sys.stdin:
    if i > 0:
        print 'Case #%s: %s'%(i, cel(line.split()[0], line.split()[1]))
    i += 1

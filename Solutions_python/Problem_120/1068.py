# bullseye.py
#
# For Google Code Jam 2013
# David Lister
#

def an(r, n):
    return (r + 2 * n + 1)**2 - (r + 2*n)**2

def s(r, n):
    return (n*(an(r, 0) + an(r, n-1)))/2.0

def paint(radius, mililiters):
    num = 0
    r = radius
    n = 0
    lo = [s(r, n), 0]
    hi = [s(r, n + 1), 1]
    over = False
    while not over:
        if lo[0] <= mililiters and hi[0] > mililiters and hi[1] - lo[1] == 1:
            over = True            
            
        elif hi[0] <= mililiters:
            n = hi[1] * 2
            lo = hi
            hi = [s(r, n), n]

        elif s(r, (hi[1] + lo[1])/2) > mililiters:
            n = (hi[1] + lo[1])/2
            hi = [s(r, n), n]

        else:
            n = (hi[1] + lo[1])/2
            lo = [s(r, n), n]

##    print hi, lo
    return lo[1]

   
fname = raw_input('Please enter file name: ')
fout = str(fname.split('.')[0]) + '.txt'

f = list(open(fname, 'r'))

lst = []
i = 1

over = False
while not over:
    try:
        lst.append(f[i][:-1].split(' '))
        i += 1
    except:
        over = True


output = ''
i = 1
for case in lst:
##    print case,
    output = output + 'Case #' + str(i) + ': ' + str(paint(int(case[0]), int(case[1]))) + '\n'
##    print 'Case #' + str(i) + ': ' + str(paint(int(case[0]), int(case[1]))) + '\n'
    i += 1

out = open(fout, 'w')
out.write(output)
out.close()

print output



#!/usr/bin/python3.1

def gcd(a,b):
    while b:      
        a, b = b, a%b
    return a

fi = open('inp111.in', 'r')
fo = open('out.txt', 'w')

for case in range(int(fi.readline())):

    stri = fi.readline().rstrip()
    stri = stri.split(" ")

    n = int(stri[0])

    events = []
    for i in range(n):
        events.append(int(stri[i+1]))

    events.sort()
    gc = abs(events[n-1] - events[0])

    for i in range(n-2):
        if events[0] != events[i+1]:
            gc = gcd(gc, abs(events[i+1] - events[0]))

    rem = 0
    if gc == 1:
        rem = 0
    elif gc == 0:
        rem = 0
    else:             
        rem = (events[0])%gc
        if rem != 0:
            rem = gc - rem

    fo.write('Case #%d: %d\n' % (case+1, rem))

fi.close()
fo.close()

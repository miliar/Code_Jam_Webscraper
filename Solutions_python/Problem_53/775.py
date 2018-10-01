f = open('/Users/michaelcoughlin/jam/small.in')
f = open('/Users/michaelcoughlin/jam/A-large.in')

first = f.readline()
cases = int(first)

for case in range(cases):
    line = f.readline()
    snappers, snaps = [ long(x) for x in line.split()]

    frequency = 2**snappers
    cycle_spot = snaps % frequency

    on = (cycle_spot + 1) == frequency


    #print snappers, snaps
    print 'Case #%s: %s' % (case+1, on and 'ON' or 'OFF')

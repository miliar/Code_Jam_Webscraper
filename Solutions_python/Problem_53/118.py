d = {True: "ON", False: "OFF"}

def calculate(snappers, snaps):
    cycle_size = (2**snappers)
    cycle_step = snaps % cycle_size
    
    return d[cycle_step == cycle_size - 1]

for case_number in xrange(int(raw_input())):
    n, k = map(int, raw_input().split())
    
    result = calculate(n, k)
    print 'Case #%d: %s' % (case_number+1, result)
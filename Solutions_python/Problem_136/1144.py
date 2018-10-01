import os
f_inp = 'inp_2_large.txt'
f_out = 'out_2_large.txt'
f=open(f_inp)
f_o = open(f_out, 'w')
def next_line(f):
    line = f.readline()
    if line:
        line = line.strip()
    return line
    
def solve(c, f, x, n_offset=0):
    #print 'offset is ', n_offset
    farms = n_offset
    last_time = x/(2+farms*f) + c*sum([1/(2+_*f) for _ in range(0,farms)])
    n = 1
    while True:
        farms = n_offset + n
        new_time = x/(2+farms*f) + c*sum([1/(2+_*f) for _ in range(0,farms)])
        #print n, new_time
        if new_time > last_time:
            if n > 3:
                return solve(c, f, x, n_offset + n/4)
            elif n > 1:
                return solve(c, f, x, n_offset + n/2)
            return last_time
        else:
            last_time = new_time
            n *= 2
        #print n, last_time
    return 0

def solve_1(c, f, x):
    last_time = x/2.0
    n = 1
    while True:
        farms = n
        new_time = x/(2+farms*f) + c*sum([1/(2+_*f) for _ in range(0,farms)])
        if new_time > last_time:
            #print n, last_time
            return last_time
        else:
            last_time = new_time
            n += 1
        #print n, last_time
    return 0


num_tc = int(next_line(f))
resp = 'Case #%s: %s'
for i in xrange(1,num_tc+1):
    row = next_line(f).split(' ')
    C,F,X = [float(_) for _ in row]
    ans = solve(C, F, X)
    out = resp % (i, ans)
    f_o.write('%s\n' % out)
    print out
f.close()
f_o.close()

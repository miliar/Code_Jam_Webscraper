'''
Created on Apr 12, 2014

@author: jirasch
'''

def solve(case):
    c, f, x = [float(x) for x in case[0].split(' ')]
    
    a = 2
    ntime = 0
    while True:
        ntime1 = c / a
        ntime1 = (x / (a + f)) + ntime1
        ntime2 = x / a
        if ntime2 < ntime1:
            return '%.7f' % (ntime + ntime2)
        else:
            ntime += (c / a) 
            a += f

if __name__ == '__main__':    
    afile = file('B-large.in')
    lines = afile.read().splitlines()
    afile.close()
    
    num = int(lines[0].strip())
    size_per_case = 1
    cases = [lines[(1 + (i * size_per_case)):(1+ (i * size_per_case)) + size_per_case] for i in range(num)]
    i = 1
    for c in cases:
        print 'Case #%d: %s' % (i, solve(c))
        i += 1

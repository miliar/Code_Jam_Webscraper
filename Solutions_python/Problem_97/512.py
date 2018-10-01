def rotations(n, d):
    r = [n]
    for i in range(1, d):
        nr = (r[-1] % 10) * (10**(d-1)) + (r[-1] / 10)
        if nr not in r:
            r.append(nr)
    return r

def number_n_m(n, l, max_num):    
    return [(n, x) for x in l if x > n and x <= max_num]
    
def solve_tc(a, b):
    r = 0
    digits = len(str(b))    
    
    #import pdb; pdb.set_trace()
    for n in range(a, b+1):
        rot    = rotations(n, digits)
        tuples = number_n_m(n, rot, b) 
        r += len(tuples)
    return r
    
def load(filename):
    l = open(filename).readlines()
    l = l[1:]
    l = [line.split(' ') for line in l]
    l = [(int(a), int(b)) for (a,b) in l]
    
    return l
    
def solve(filename, outputfilename):
    l = load(filename)
    f = open(outputfilename, "w")
    
    for n,line in enumerate(l):
        print n+1
        f.write("Case #" +  str(n+1) + ": " + str(solve_tc(*line)) + '\n')
    
    f.close()
        

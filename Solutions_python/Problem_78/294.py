import sys

def simplify(percent):
    if percent == 0:
        return [0, 0]
    
    a = percent
    b = 100
    
    div = 2
    run = True
    
    while run:
        if a % div == 0 and b % div == 0:
            a /= div
            b /= div
        else:
            div += 1
            
        if div > min(a, b):
            run = False 
        
    return [a, b]

input = sys.stdin
cases = int(input.readline())

def calculate(N, PD, PG):
    possible = False
    
    if (PG == 100 and PD != 100) or (PD == 100 and PG == 0):
        return False

    pd_frac = simplify(PD)
    pg_frac = simplify(PG)

    possible_d = pd_frac[1]
    possible_g = pg_frac[1]
    
    if possible_d <= N and possible_d <= possible_g:
        possible = True

    return possible

for case in xrange (cases):
    N, PD, PG = map(int, input.readline().strip().split(" "))
    
    possible = calculate(N, PD, PG)
    
    output = "Broken"
    if possible:
        output = "Possible"
        
    print "Case #%d: %s" % (case + 1, output)

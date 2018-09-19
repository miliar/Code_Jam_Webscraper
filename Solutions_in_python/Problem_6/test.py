import sys, math

def a_and_b(n):
    a = 3
    b = 1
    for x in xrange(n-1):
        a_tmp = a
        a = 3*a + 5*b
        b = a_tmp + 3*b
    return last_three(a, b)
    #print a, b


def last_three(a, b):
    #print a, b
    b_three = int(math.sqrt(b*b*5)) % 1000
    
    b_sqrt5 = math.sqrt(b*b*5)
    
    #print b_sqrt5
    b_5tmp = int(b_sqrt5)
    if b_5tmp * b_5tmp > b*b*5:
        
        tmp = b_5tmp
        while tmp* tmp > b*b*5:
            tmp = tmp-1
        
        b_three = tmp
    
    return (b_three + a) % 1000

def process(r):
    val_str = r.readline()
    val = int(val_str)
    #print val
    return a_and_b(val)

def main():
    if len(sys.argv) > 1:
        r1 = open(sys.argv[1])
        cases_str = r1.readline()
        cases  = int(cases_str)
        
        for x in xrange(cases):
            val = process(r1)
            
            print "Case #%d: %03d"%(x+1, val)
main()
a_and_b(30)

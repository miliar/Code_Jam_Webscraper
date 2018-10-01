import sys

def case_iterator(path):
    with file(path) as f:
        lines = iter(f)
        n = int(lines.next())
        
        for i in range(1, 1 + n):
            yield i, read_case(lines)
    
def read_case(lines):
    n = int(lines.next().strip())
    return n
    
def gcd(x,y):
    if x < y:
        return gcd(y,x)
    
    if y == 0:
        return x
    
    return gcd(y, x % y)

def LCM(x,y):
    return x * y / gcd(x,y)  
    
def calc_up(n):
    lcm = 1
    
    total = 1
    
    for i in xrange(1, n + 1):
        if lcm % i != 0:
            total += 1
            lcm = LCM(lcm, i)
            
    return total

def calc_down(n):
    lcm = n
    total = 1
    
    for i in xrange(n - 1, 1, -1):
        if lcm % i != 0:
            total += 1
            lcm = LCM(lcm, i)
            
    return total

def is_prime(n):
    for i in xrange(2, n):
        if n % i == 0:
            return False
        
    return True

def calc_prime(n):
    if n ==1:
        return 1
    
    total = 0
    
    for i in xrange(2, n+1):
        if is_prime(i):
            total += 1
            
    return total
    

    
def solve(case):
    n = case
    max_w = calc_up(n)
    #min_w = calc_down(n)
    min_w = calc_prime(n)
    return max_w - min_w
    
def main():
    try:
        path, = sys.argv[1:]
    except ValueError:
        sys.exit('usage: %s <input file>' % (sys.argv[0],))
    
    for i, case in case_iterator(path):
        print 'Case #%d: %s' % (i, solve(case))
        

if __name__ == '__main__':
    main()

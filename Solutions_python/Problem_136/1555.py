
def solve():
    c,f,t = [float(x) for x in raw_input().strip().split()]
    s = 2
    i = 0
    mult = 0.5
    best = t/s
    while True:
        x = mult*c + t/(s+(i+1)*f)
        if x > best: return best
        best = x
        mult += 1/(s+(i+1)*f)
        i += 1
        
def main():
    n = input()
    for i in xrange(n):
        x = solve()
        print "Case #%s: %f" %((i+1),x) 

if __name__=='__main__':
    main()

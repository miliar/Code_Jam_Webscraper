
def solve_problem(c,f,x):
    roi = c/f
    rate = 2.0
    count = 0
    t = 0
    ttw = (x-count)/rate
    while (ttw > c/rate+(x/(rate+f)) ):
        count = 0
        t += (c/rate)
        rate +=f
        ttw = (x-count)/rate
    ttw = t + (x-count)/rate
    return ttw
def main():
    ncases = int(raw_input())
    for i in xrange(ncases):
        (c,f,x) = [float(f) for f in raw_input().split(" ")]
        print "Case #%d: %f"%(i+1, solve_problem(c,f,x))

if __name__ == '__main__':
    main()

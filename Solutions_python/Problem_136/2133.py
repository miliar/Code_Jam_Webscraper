import sys

infile = open(sys.argv[1], 'rb')
outfile =open('out.txt', 'wb')
n = int(infile.next())

for n_i in xrange(n):
    c, f, x = [float(val) for val in infile.next().split()]
    rate = 2.
    y = 0
    while (c/rate+x/(rate+f)) < x/rate:
        y += c/rate
        rate += f
    y += x/rate
    outfile.write('Case #%s: %.7f\n' %((n_i+1), y))

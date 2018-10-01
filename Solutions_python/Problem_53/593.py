filename = "A-large.in"
f = open (filename)
outfile = open (filename.rsplit(".", 1)[0] + ".out", 'w')

T = int(f.readline())

for i in xrange(T):
    l = [int(x) for x in f.readline().split(" ")]
    N = l[0]
    K = l[1]
    
    if K & ((2**N)-1) == (2**N)-1:
        outfile.write("Case #%d: ON\n" % (i+1))
    else:
        outfile.write("Case #%d: OFF\n" % (i+1))

    

f.close()
outfile.close()

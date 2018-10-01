#Filename: snapper.py

infile = open("A-large.in")
outfile = open("output.txt", 'w')

things = (infile.read()).split()
things.pop(0)
i=1

while len(things) >= 2:
    N = int(things.pop(0))
    K = int(things.pop(0))

    algo = 1
    
    for j in range(0,N):
        algo *= 2

    if K == algo-1:
        outfile.write("Case #%d: ON\n" % i)
    elif (K-algo+1)%algo == 0:
        outfile.write("Case #%d: ON\n" % i)
    else: outfile.write("Case #%d: OFF\n" % i)

    i+=1

infile.close()
outfile.close()


import sys

infile = open(sys.argv[1])
outfile = open("A-small.out", "w")
number = infile.readline()

for i, line in enumerate(infile):
    n, k = line.strip().split(" ")
    n, k = int(n), int(k)
    magic = pow(2, n) - 1

    if (k == magic):
        outfile.write("Case #{0}: ON\n".format(i+1))
    elif (k > magic) and ((k - magic) % pow(2,n) == 0):
        outfile.write("Case #{0}: ON\n".format(i+1))
    else:
        outfile.write("Case #{0}: OFF\n".format(i+1))

              

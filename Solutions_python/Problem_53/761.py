import sys

def main() :
    if (len(sys.argv) != 2) :
        print sys.argv[0] + " [input file]"
        return

    input = open(sys.argv[1])

    limit = int(input.readline())
    print "Handling " + str(limit) + " cases."

    output = open("output.txt", "w")

    for ii in xrange(0, limit, 1) :
        line = input.readline()
        # strip new line
        line = line[:-1]
        line = line.split()
        N = int(line[0])
        K = int(line[1])
        TwoToN = 2**N
        K %= TwoToN
        if (K == (TwoToN - 1)) :
            output.write("Case #" + str(ii + 1) + ": ON\n")
        else :
            output.write("Case #" + str(ii + 1) + ": OFF\n")

    input.close()
    output.close()

if __name__ == "__main__" :
    main()

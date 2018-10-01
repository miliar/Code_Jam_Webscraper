"""Code Jam - Recycled Numbers

Solution to Google Code Jam 2012 Qualification Round Problem C
"""

import sys

def main(argv=None):

    # Setup arguments
    if argv is None:
        argv = sys.argv

    # Setup IO
    fin = open(argv[1], 'r')
    fout = open(argv[0] + '.out', 'w')

    # Read in data
    casesCount = fin.readline()
    cases = fin.readlines()

    # Process each case
    i = 1
    for case in cases:
        data = case.split(' ')

        # Parse out parameters
        A = int(data[0])
        B = int(data[1])

        sumRecycles = 0

        # Find sum of recycles
        caseRange = range(A,B)

        for n in caseRange:
            m = list(str(n))
            for j in range(0, len(m)):
                m.insert(0, m.pop())
                im = int(''.join(m))
                sumRecycles += n < im and im <= B

        fout.write("Case #%d: %d\n" % (i, sumRecycles))
        print "Case #%d: %d" % (i, sumRecycles)
        i += 1

    fin.close()
    fout.close()

if __name__ == "__main__":
    sys.exit(main())

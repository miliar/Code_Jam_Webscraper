import sys
import numpy as np

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    if len(argv) >= 1:
        inFileName= argv[0]
    else:
        inFileName = "test.in"
    if len(argv) >= 2:
        outFileName = argv[1]
    else:
        outFileName = "out.out"

    with open(inFileName) as inFile:
        with open(outFileName, 'w') as outFile:
            for caseNo, line in enumerate(inFile):
                if caseNo == 0:
                    numCases = int(line)
                    continue
                toks = line.split()

                C = int(toks[0])
                cc = toks[1:C+1]
                D = int(toks[C+1])
                dd = toks[C+2:C+D+2]
                N = int(toks[-2])
                seq = toks[-1]

                combs = {}
                makes = {}
                opps = {}

                for c in cc:
                    combs.setdefault(c[0], set())
                    combs.setdefault(c[1], set())
                    combs[c[0]].add(c[1])
                    combs[c[1]].add(c[0])
                    makes[c[:2]] = c[2]
                    makes[c[1::-1]] = c[2]

                for d in dd:
                    opps.setdefault(d[0], set())
                    opps.setdefault(d[1], set())
                    opps[d[0]].add(d[1])
                    opps[d[1]].add(d[0])

                elts = []
                for elt in seq:
                    c = combs.setdefault(elt, set())
                    if elts and elts[-1] in c:
                        elts[-1] = makes[elts[-1] + elt]
                        continue 

                    o = opps.setdefault(elt, set())
                    if not o.isdisjoint(elts):
                        elts = []
                        continue

                    elts.append(elt)
                outFile.write("Case #{0}: [".format(caseNo))
                for elt in elts[:-1]:
                    outFile.write("{0}, ".format(elt))
                if elts:
                    outFile.write("{0}]\n".format(elts[-1]))
                else:
                    outFile.write("]\n")

            if numCases != caseNo:
                print "Missing Case!"


if __name__ == "__main__":
    main()

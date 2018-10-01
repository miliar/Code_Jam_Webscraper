import argparse
import sys

def jam(inFile, outFile):
    T = int(getline(inFile))
    for c in range(T):
        ints = [int(x) for x in getline(inFile).split(' ')]
        case(ints[0], ints[1], ints[2], ints[3:], c+1, outFile)

def std_best(n): return (n//3) + (1 if not n % 3 == 0 else 0)
def sur_best(n): 
    if n > 3:
        return (n//3) + (1 if not n % 3 == 2 else 2)
    return min(n, 2)

def case(n, s, p, t, caseNum, outFile):
    std_above = set([])
    sur_above = set([])
    always_below = set([])

    for i in range(n):
        if std_best(t[i]) >= p:
            std_above.add(i)
        elif sur_best(t[i]) >= p:
            sur_above.add(i)

    max = len(std_above) + min(len(sur_above), s)
    out = "Case #{}: {}".format(caseNum, max)
    outFile.write(out + "\n")
    print(out)

def getline(stream):
    return stream.readline().strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', dest='file')
    
    args = parser.parse_args(sys.argv[1:])

    f = open(args.file, 'r')
    o = open(args.file + ".out", 'w')

    jam(f, o)

    o.flush()
    o.close()
    f.close()

main()

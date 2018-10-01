import argparse
import sys

dict = {
    ' ' : ' ',
    'a' : 'y',
    'b' : 'h',
    'c' : 'e',
    'd' : 's',
    'e' : 'o',
    'f' : 'c',
    'g' : 'v',
    'h' : 'x',
    'i' : 'd',
    'j' : 'u',
    'k' : 'i',
    'l' : 'g',
    'm' : 'l',
    'n' : 'b',
    'o' : 'k',
    'p' : 'r',
    'q' : 'z',
    'r' : 't',
    's' : 'n',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'x' : 'm',
    'y' : 'a',
    'z' : 'q'
}

def jam(inFile, outFile):
    T = int(getline(inFile))
    for i in range(T):
        case(getline(inFile), i+1, outFile)

def case(line, caseNum, outFile):
    outFile.write("Case #{}: {}\n".format(caseNum, ''.join([dict[x] for x in line])))

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

import sys
import math

infile = open(sys.argv[1])

def read_in(infile):
    data = infile.readlines()
    case_cnt = int(data[0])
    ranges = [line.split() for line in data[1:]]
    assert case_cnt == len(ranges)
    return ranges


def palindrome(w):
    # the compare the reverse of the string
    return str(w) == str(w)[::-1]



def how_many(a, b):
    a_base = int(math.ceil(math.sqrt(int(a))))
    b_base = int(math.floor(math.sqrt(int(b))))
    fscount=0
    #fs = []
    for x in range(a_base, b_base+1):
        if not palindrome(x):
            continue
        if palindrome(x**2):
            fscount=fscount+1
            #fs.append(x)
    return fscount



def main():
    
    ranges = read_in(infile)
    
    for case, (a, b) in enumerate(ranges):
        print ('Case #%s: %s' % (case+1, how_many(a,b)))
    
    



if __name__=='__main__':
    main()
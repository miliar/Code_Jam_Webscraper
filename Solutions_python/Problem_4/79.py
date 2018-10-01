TEST = False
FILENAME = "A-small-attempt0.in"
FILENAME = "A-large.in"

def main():
    def p(line):
        print line
        fo.write(line + "\n")

    if TEST:
        fi = file("sample")
    else:
        fi = file("/Users/nishio/Desktop/" + FILENAME)
    fo = file("/Users/nishio/0", "w")

# main code here
    UPPER_BOUND = 10000 
    num_test = int(fi.readline())
    for test_id in range(num_test):
        fi.readline() # num of elements. no needs
        vec1 = map(int, fi.readline().split())
        vec2 = map(int, fi.readline().split())
        print vec1
        print vec2
        vec1.sort()
        vec2.sort(reverse=True)
        from operator import add, mul
        result = reduce(add, map(mul, vec1, vec2))
        p("Case #%d: %d" % (test_id + 1, result))
    
    fi.close()
    fo.close()

#import doctest
#doctest.testmod()
main()


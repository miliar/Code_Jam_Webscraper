import sys
import math

palindromes = set()
fairs = set()
fair_count = {}

def is_pal(x):
    if x in palindromes:
        return 1
    z = str(x)
    length = len(z)
    if length == 1:
        return 1

    l=length/2

    if z[:l]==z[-l:][::-1]:
        palindromes.add(x)
        return 1
    return 0

def is_my_square_fair(small):
    big = small**2
    if big in fairs:
        return True
    if is_pal(small) and is_pal(big):
        fairs.add(big)
        return True
    return False


def get_pal_range(a, b):
    start = int(math.ceil(math.sqrt(a)))
    end = int(math.floor(math.sqrt(b)))
    counter = 0
 #   print a,b
    for small in xrange(start, end+1):

        if is_pal(small):
            big = small ** 2
            if is_pal(big):
                fairs.add(big)
#                print big
                counter += 1
        #if is_my_square_fair(small):
#            counter += 1

    #print
    #print
    return counter



def scan_whole(checkpoints):
    checkpoints = list(checkpoints)
    checkpoints.sort()

    #print "Checkpoints"
    #print checkpoints

    d = {}
    a = 1
    b = max(checkpoints)
    start = int(math.ceil(math.sqrt(a)))
    end = int(math.ceil(math.sqrt(b)))
    counter = 0
    #   print a,b
    for small in xrange(1, end+1):
        #print "Small:", small
        if is_pal(small):
            big = small ** 2
            if is_pal(big):
                fairs.add(big)

                while checkpoints[0] < big:
                    item = checkpoints.pop(0)
                    d[item] = counter

                counter += 1

                if checkpoints[0] == big:
                    item = checkpoints.pop(0)
                    d[item] = counter

                #print checkpoints
                #print
    while checkpoints:
        item = checkpoints.pop(0)
        d[item] = counter

    #for key in sorted(d.iterkeys()):
#        print key, "-", d[key]

    return d




    #return counter

def parse_input(inputfile):
    f = open(inputfile)
    o = open(inputfile + "-out.txt", "w")
    pairs = []

    checkpoints = set()
    numLines = int(f.readline())
    for i in xrange(1, numLines + 1):
        a, b = map(int, f.readline().strip().split(" "))
        pairs.append((a,b,))
        checkpoints.add(a)
        checkpoints.add(b)



        #result = get_pal_range(a, b)
        #o.write("Case #%d: %d\n" % (i, result))
    #o.close()
    f.close()
    d = scan_whole(checkpoints)
    for i,pair in enumerate(pairs):
        a, b = pair

        result = d[b] - d[a]
        if a in fairs:
            result += 1

        o.write("Case #%d: %d\n" % (i+1, result))
    o.close()


if __name__ == "__main__":
    parse_input(sys.argv[1])


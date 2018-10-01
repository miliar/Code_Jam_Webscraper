import sys

f = open(sys.argv[1])

num_cases = int(f.readline().rstrip())
for case in range(1,num_cases + 1):
    num_elements = int(f.readline().rstrip())
    xa = [int(z) for z in f.readline().strip().split()]
    num = len([(x,y) for x,y in zip(xa, sorted(xa)) if x!=y])
    print "Case #%d: %f" % (case, num)

import sys
with open(sys.argv[1]) as f:
    T = int(f.readline().strip())
    for i in range(T):
        f.readline()
        nums = [int(x) for x in f.readline().strip().split()]
        wrong = sum(n!=i for n, i in enumerate(nums, 1))
        print "Case #%d:" % (i+1), float(wrong)

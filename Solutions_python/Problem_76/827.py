import sys, os, operator

cases = int(sys.stdin.readline())

for case in xrange(cases):
    n = int(sys.stdin.readline())
    nums = map(int, sys.stdin.readline().split())
    if (reduce(operator.xor, nums)):
        print 'Case #%d: NO' % (case + 1)
        continue
    maxsum = 0
    nums.sort()
    maxsum = reduce(operator.add, nums[1:])
    print 'Case #%d: %d' % (case + 1, maxsum)

            

                
    

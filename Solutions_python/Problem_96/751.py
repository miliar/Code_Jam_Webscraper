__author__ = 'Sebastian Poreba'

N = int(raw_input())

for i in xrange(0, N):
    input = [int(x) for x in (raw_input().split())]
    triplets_count = input[0]
    surprising = input[1]
    above = input[2]
    triplets = input[3:]
    if above == 0:
        print 'Case #%d: %d' % (i+1, triplets_count)
        continue
    safe_triplets = [x for x in triplets if x >= above*3-2]
    others =  [x for x in triplets if x < above*3-2]

    unsafe_triplets = [x for x in others if x >= above*3-4 and x > 2]


#    print surprising, above, safe_triplets, unsafe_triplets

    print 'Case #%d: %d' % (i+1, len(safe_triplets) + min(len(unsafe_triplets), surprising))
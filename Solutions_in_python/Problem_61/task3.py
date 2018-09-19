#!/usr/bin/env python2.6

in_file = 'C-test.in'
out_file = 'C-test.out'
in_file = 'C-small-attempt1.in'
out_file = 'C-small.out'
in_file = 'C-large.in'
out_file = 'C-large.out'

from scipy.misc.common import comb


#def combis(num_slots, num_options):
#    if num_slots == 0:
#        return 1
#    else:
#        tot = 1
#        cur_opt = num_options
#        for i in range(0, num_slots):
#            tot = tot * cur_opt
#            cur_opt = cur_opt - 1
#        return tot

def get_count(n, size,memo):
    if n == 7 and size == 4:
        pass
    if not memo.has_key((n,size)):
        tot_count = 0
        l = max(1,size - (n - size))
        r = size-1
        for a in range(l, r+1):
            count = get_count(size, a, memo)
            tot_count = tot_count + (count * comb(n-size-1,size-a-1,1))
        memo[(n,size)] = tot_count
    return memo[(n,size)]


with open(in_file) as input:
    with open(out_file, 'w') as output:
        T = int(input.readline().rstrip())

        memo = {}
        for n in range(1, 501):
            memo[(n,1)] = 1



        for t in range(1,T+1):

            n = int(input.readline().rstrip())

            tot_count = 0
            for s in range(1,n):
                count = get_count(n, s,memo)
                tot_count = tot_count + count

            tot_count = tot_count % 100003
            
            
            print >> output, 'Case #%d: %s' % (t,tot_count)


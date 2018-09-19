#!/usr/bin/python

__author__ = "Thomas van den Berg"

import math

fact = math.factorial
e    = math.e

fn = 'D-small-attempt2.in'
f = open(fn,'r')
fout = open(fn.replace('.in','.out'),'w')


# Essentially this amounts to a selection sort, minimizing the number
# of swaps. It is optimal for Goro to always hold all but 2 items, as a permutation
# of 3 items will always take longer to order than 2 permutations of 2 items,
# and the same reasoning goes for 3+ items.

# T = int(f.readline())
# for case in xrange(T):
#     N     = int(f.readline())
#     a     = [int(num) for num in f.readline().split()]
#     swaps = 0
#     print "Case %d"%(case+1)
#     for j in xrange(len(a)):
#         m = a.index(min(a[j:]))
#         print a 
#         if m != j:
#             swaps += 1
#             a[j],a[m] = a[m],a[j]
#         
#     print "Ans: %d"%(swaps*2)
#     ans = swaps*2
#     
#     fout.write('Case #%d: %.6f\n'%(case+1,ans))

# Forget about that. Shuffling 2+ items leads to an average of more than 
# 1 item landing in place! So shuffling is actually better! 
# Goro should always hold only those items that are already in place. 
# Shuffling 2 always leads to a maximum of 2 items landing in place, with probability 0.5.
# Shuffling 3 items already has probability 0.5 of landing 1 item in place, and 1/6 
# of ordering all three items!
# Number of permutations that lead to x out-of-place items for:
# x = | 0    1    2    3    4    5    6
# ----+----------------------------------
# n=1 | 1    0
# n=2 | 1    0    1
# n=3 | 1    0    3    2
# n=4 | 1    0    6    8    9
# n=5 | 1    0   10   20   45   44
# n=6 | 1    0   15   40  135  264  265

# Apparently this 0, 1, 2, 9, 44 is called a subfactorial. Learned something new XD.
# Apparently they can be computed for k = (n-x) by: nchoosek(n,k) * int((n-k)!/e)

# k =    0    1    2   3   4  5  6
# ------------------------     
#        0    1                
#        0    0                
# ------------------------     
#        1    0    1           
#        0    0    0           
# ------------------------     
#        2    3    0   1       
#        2    0    0   0       
# ------------------------     
#        9    8    6   0   1   
#        8    8    0   0   0   
# ------------------------     
#       44   45   20  10   0  1
#       44   40   20   0   0  0
# ------------------------     
#      265  264  135  40  15  0  1
#      264  264  120  40   0  0  0

# Somehow the terms for which (n-k) is EVEN are off. But they are off by nchoosek(n,k)! 
# So there we go:

def n_in_place(n,k):
    # return (fact(n) / fact(k) / fact(n-k)) * int(fact(n-k)/e)                    # By the book.
    return (fact(n) / fact(k) / fact(n-k)) * int(fact(n-k)/e + (n-k+1)%2) # Added 1 for even terms
    
# Suppose we have the function t(x) that indicates the average amount of shuffles needed
# when x items are out of place, then:
# t(0) = 0
# t(2) = 1 + 1/2*t(2) + 1/2*t(0)
# t(3) = 1 + 2/6*t(3) + 3/6*t(2) + 1/6*t(0)
# ...
# These factors are the numbers described above, so the self-recurring term (plus + 1) 
# can be computed exactly using the limit of a geometric series. And that is what we'll return too.

def t(x):
    tot = 0.0
    ps = float(fact(x))
    # Add the recursive terms
    for k in xrange(1,x-1):
        term = t(x-k)
        factor = (n_in_place(x,k)/ps)
        # print '%d/%d * (t(%d) = %.2f)'%(n_in_place(x,k),ps,x-k,term)
        tot += factor * term
    # Add the geometric series term:
    a = tot + 1
    r = n_in_place(x,0)/ps
    # print '+ 1/(1-%d/%d) = %.2f'%(num_in_place(x,0),ps,1/(1-r))
    return a/(1-r)
    
    
T = int(f.readline())
for case in xrange(T):
    N     = int(f.readline())
    a     = [int(num) for num in f.readline().split()]
    n_out_of_place = sum((1 if o!=s else 0) for (o,s) in zip(a, sorted(a)))
    
    if n_out_of_place > 0:
        ans = t(n_out_of_place)
    else: 
        ans = 0.0
    print 'ans',ans
    fout.write('Case #%d: %s\n'%(case+1,ans))
    

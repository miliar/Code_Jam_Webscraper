from sys import maxint as INF
from heapq import *

fd = open('A-large.in', 'r')
s = fd.read()
fd.close()
s = s.split('\n')

class TestCase:
    def __init__(self, P,K,L, freq_table):
        self.P = P
        self.K = K
        self.L = L
        self.freq_table = freq_table


cases = []

num_cases = int(s[0])
s = s[1:]

while len(s) > 0:
    if s[0] == '':
        s = s[1:]
        continue
    f_l = s[0].split(' ')
    P = int(f_l[0])
    K = int(f_l[1])
    L = int(f_l[2])
    freq_list = [int(x) for x in s[1].split(' ')]
    # Format: (-frequency, letter)
    f = []
    for i in xrange(len(freq_list)):
        f.append((-freq_list[i],i))
    
    heapify(f)
    
    s = s[2:]
    cases.append(TestCase(P,K,L,f))
    

counter = 0

for c in cases:
    counter += 1
    
    keypresses = 0

    P = c.P
    K = c.K
    L = c.L
    f = c.freq_table

    assigned_keys = [(0,i) for i in xrange(K)]
    
    heapify(assigned_keys)
    
    # assigned keys now has my keys sorted in order of use
    
    done = False

    while len(f) > 0:
        current_letter = heappop(f)
        freq = -current_letter[0]
        
        kta = heappop(assigned_keys)
        heappush(assigned_keys, (kta[0]+1,kta[1]))
        keypresses += freq * (kta[0]+1)


    print 'Case #%d: %d' %(counter, keypresses)

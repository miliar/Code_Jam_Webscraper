import math

i_f = open('C-small-attempt1.in', 'r')
o_f = open('C-small-attempt1.out', 'w')

tup = [1, 4, 9, 121, 484]

t = int(i_f.readline().strip())

no = 0

for i in range(t):
    a=i_f.readline().strip().split(' ')
    miv = int(a[0])
    mav = int(a[1])

    for j in tup:
        if j >= miv and j <= mav:
            no = no + 1

    o_f.write('Case #%d: %d\n' % (i+1, no))
    no = 0
    
i_f.close()
o_f.close()

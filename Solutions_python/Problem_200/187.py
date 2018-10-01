__author__ = 'Christian'

#fname = 'test_b.txt'
#fname = 'B-small-attempt0.in'
fname = 'B-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')



def compute_previous_tidy(s):
    
    tidy = ''
    current_val = 0
    still_ok = True

    for c in s:
        c = int(c)
        if still_ok:
            if c < current_val:
                tidy += '9'
                still_ok = False
                continue
            else:
                tidy += str(c)
            current_val = c
        else:
            tidy += '9'
            still_ok = False
    if still_ok:
        return s

    final = ''
    max_encountered = False
    for c in tidy:
        c = int(c)
        if c < current_val:
            final += str(c)
        elif max_encountered:
            final += '9'
        else:
            max_encountered = True
            if c > 1:
                final += str(c-1)

    return final


T = int(data[0])
for i in range(T):
    print >> res_file, "Case #%s: %s" % (i+1, compute_previous_tidy(data[i+1]))
    
res_file.close()
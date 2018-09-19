#!/usr/bin/python
def num_digits(val):
    if val < 10:
        return 1
    return 1 + num_digits(val/10)
def nr_good_vals(minval, maxval, testval):
    ndigits = num_digits(testval)
    ret = 0
    selected = []
    for x in range(minval, maxval+1):
        selected.append(0)
    for shift in range(1,ndigits):
        left = testval/(10**shift)
        right = testval%(10**shift)
        newnum = right * (10**(ndigits-shift)) + left
        if (newnum > testval) and (newnum >= minval) and (newnum <= maxval) and\
        (selected[newnum-minval] == 0):
            ret += 1
            selected[newnum-minval] = 1
    return ret
if __name__ == "__main__":
    f = open('C-small-attempt0.in', 'r')
    t = int(f.readline())
    for i in range(1, t + 1):
        val = 0
        line = f.readline()
        x = [int(s) for s in line.split()]
        A = x[0]
        B = x[1]
        for v in range(A, B+1):
            val += nr_good_vals(A,B,v)
        print "Case #"+str(i)+": "+str(val)
    f.close()
        
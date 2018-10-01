import numpy as np


def is_tidy(s):
    """"""
    tidy = True
    for i in np.arange(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            tidy = False
            break
    return tidy


def fill_nines(s):
    for i in np.arange(len(s)):
        s[i] = '9'
    return s


def make_tidy(s):
    for i in np.arange(len(s)-1):
        if not is_tidy(s[:i+2]):
            s[i+1:] = fill_nines(s[i+1:])
            if s[i] > 0:
                s[i] = str(int(s[i])-1)
            else:
                print "value was zero and would have been removed"
            make_tidy(s[:i+1])
    return s

if __name__ == '__main__':
    t = int(raw_input())
    for i in np.arange(t):
        s = raw_input()
        s = np.array([x for x in s])
        s = make_tidy(s)
        s = [x for x in s if x != '0']
        print 'Case #%d: '%(i+1)+''.join(s)


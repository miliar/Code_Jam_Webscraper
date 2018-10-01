#!/usr/bin/python

t = int(input())
for i in range(t):
    normal, nottidy, run = (False, True, 0)
    ln = input()
    iln = int(ln)

    if len(ln) > 1:
        if '0' in ln:
            for j in range(len(ln)):
                if ln[j] != 1 and ln[j] != 0:
                    normal = True
            if not normal:
                ln = '9' * (len(ln)-1)
                iln = int(ln)
            elif ln[0] > ln[1]:
                ln = str(int(ln[0])-1) + ('9'*(len(ln) - 1))
                iln = int(ln)
            else:
                iln = iln - int(ln[j]) - 1
        else:
            j = 0
            while nottidy:
                if j < (len(ln) - 1):
                    if ln[j] > ln[j+1]:
                        if j == 0:
                            ln = str(int(ln[0])-1) + ('9'*(len(ln) - 1))
                            iln = int(ln)
                        else:
                            iln = iln - int(ln[j+1]) - 1
                        ln = str(iln)
                    j += 1
                else:
                    run += 1
                    if run == (len(ln) - 1):
                        nottidy = False
                    else:
                        j = 0

    print('Case #%s: %d' % (i+1, iln))

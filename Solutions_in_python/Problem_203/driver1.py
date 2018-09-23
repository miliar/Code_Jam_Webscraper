from __future__ import print_function
import numpy as np
# from collections import

# Fernando Gonzalez del Cueto. Code Jam 2017

#infile = 'test.in'
infile = 'A-small-attempt1.in'

outfile = infile.replace('.in', '.out')

fid = open(infile, 'r')

n_cases = int(fid.readline().strip())

f_out = open(outfile, 'w')

def solver(a, chars):

    n_rows, n_cols = a.shape
    assert isinstance(a, np.ndarray)
    assert isinstance(chars, set)

    for char in chars:

        i,j = np.argwhere(a==char)[0]

        b = np.zeros_like(a, dtype=np.bool)
        b[a==char] = True
        b[a=='?'] = True


        pos = []
        for i1 in range(0,i+1):
            for i2 in range(i+1, n_rows+1):
                for j1 in range(0,j+1):
                    for j2 in range(j+1,n_cols+1):
                        if b[i1:i2, j1:j2].all():
                            pos.append((i1,i2,j1,j2,(i2-i1)*(j2-j1)))
                        else:
                            break

        pos.sort(key=lambda(x):-x[-1])

        # best answer
        i1,i2,j1,j2,size = pos[0]
        a[i1:i2,j1:j2] = char

    return a, b, pos


def array_to_str(a):

    assert isinstance(a, np.ndarray)
    s = ''
    m,n = a.shape
    for i in range(m):
        for j in range(n):
            s += '%s' % a[i,j]
        s += '\n'
    return s


for test_case in range(n_cases):

    rows, cols = map(int, fid.readline().strip().split())

    l = []
    chars = set()
    for i in range(rows):
        line = list(fid.readline().strip())
        chars.update(set(line))
        l.append(line)

    a = np.array(l, dtype=str)
    a0 = a.copy()

    if '?' in chars:
        chars.remove('?')
        sol, _, _ = solver(a, chars)
    else:
        sol = a

    #sol = find_improv(b)

    sol_s = array_to_str(sol)

    l = 'Case #%i:\n%s' % (test_case + 1, sol_s)
    print('case #%i' % test_case)
    print(array_to_str(a0))
    print(sol_s)
    f_out.write(l)
    print(sol)


f_out.close()
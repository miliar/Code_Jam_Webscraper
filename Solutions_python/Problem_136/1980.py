import sys
import time
import os


def read_lines(file_in):
    with open(file_in) as f:
        content = f.read()
    lines_in = content.splitlines()
    return lines_in


def write_lines(lines_out, file_out):
    with open(file_out, 'w') as f:
        f.writelines(lines_out)


def take_mat(bgn, lines_in):
    mat = []
    for ind in range(4):
        mat.append(set(map(int, lines_in[ind + bgn].split(' '))))
    return mat

#############################################################################

# file_in = 'sample.in'
# file_in = 'B-small-attempt1.in'
file_in = 'B-large.in'

filename, _ = os.path.splitext(file_in)
file_out = filename + '.out'

lines_in = read_lines(file_in)
num_cases = int(lines_in[0])

V = 2.0
#############################################################################

lines_out = []

def solve_now(X_now, V_now, C, F, X):

    T_rem = (X - X_now) / V_now

    if T_rem * F <= C:
        return T_rem
    else:
        return C / (V_now + F) + \
            solve_now(X_now=C, V_now=(V_now + F), C=C, F=F, X=X)






for ind in range(num_cases):

    C, F, X = map(float, lines_in[ind + 1].split(' '))

    # # speed test
    # X = 100000.

    if X <= C:
        T = X / V
    else:
        V_now = V

        T_rem = (X - C) / V_now

        T = C / V

        while T_rem * F > C:
            V_now += F
            T = T + C / V_now

            T_rem = (X - C) / V_now
        

        T = T + T_rem

            


        # T = C / V + solve_now(X_now=C, V_now=V, C=C, F=F, X=X)

    lines_out.append("Case #%d: %.7f\n" % (ind + 1, T))

#############################################################################

write_lines(lines_out, file_out)

# lines_out = []
# for ind in range(num_cases):
#     lines_out.append("Case #%d:\n" % (ind + 1))
# write_lines(lines_out, file_out)
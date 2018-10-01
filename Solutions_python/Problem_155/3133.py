import re

#turn a file into a generator for shyness dictionaries
def get_shy_gen(filename):
    f = open(filename, 'r')
    nlines = int(re.search(r'(\d+)', next(f)).group(1))
    for n, line in enumerate(f):
        if n < nlines:
            yield {i : int(c) for i, c in enumerate(re.search(r'(\d+)', line.split(' ')[1]).group(1))}


def find_invites(shy):
    crowd = 0
    invites = 0

    for i in range(max(shy) + 1):
        if crowd < i:
            invites += i - crowd
            crowd += i - crowd
        crowd += shy[i]
    
    return invites

def solve_prob(filein, fileout):
    g = get_shy_gen(filein)
    f = open(fileout, 'w')
    for i, shy in enumerate(g):
        invites = find_invites(shy)
        f.write('Case #' + str(i + 1) + ': ' + str(invites) + '\n')

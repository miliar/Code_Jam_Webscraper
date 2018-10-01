# Fernando Gonzalez del Cueto. Code Jam 2017

#infile = 'test.in'
#infile = 'A-small-attempt0.in'
infile = 'A-large.in'
outfile = infile.replace('.in', '.out')

fid = open(infile, 'r')

n = int(fid.readline().strip())

f_out = open(outfile, 'w')

def stringify(l):
    return ''.join(map(lambda(x):'+' if x else '-', l))

def solve(s, k):

    if s == '+'*len(s):
        return '0'
    else:
        print(s)
        l = [c=='+' for c in s]

        flips = 0

        impossible = True

        for j in range(len(s)-k+1):
            print('%5i, %i: %s' % (j, flips, stringify(l)))
            if l[j] == True:
                pass
            else:
                # flip
                l[j:j+k] = map(lambda(x):x==False, l[j:j+k])
                flips += 1

        print('%5i, %i: %s' % (j, flips, stringify(l)))

    if all(l):
        return str(flips)
    else:
        return 'IMPOSSIBLE'

for i in range(n):

    s, k_s = fid.readline().strip().split()
    k = int(k_s)

    sol = solve(s, k)

    l = 'Case #%i: %s\n' % (i + 1, sol)
    f_out.write(l)
    print(sol)

f_out.close()
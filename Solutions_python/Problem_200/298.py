# Fernando Gonzalez del Cueto. Code Jam 2017

#infile = 'test.in'
#infile = 'B-small-attempt0.in'
infile = 'B-large.in'
outfile = infile.replace('.in', '.out')

fid = open(infile, 'r')

n = int(fid.readline().strip())

def find_tidy(s):
    n = len(s)

    l = [int(c) for c in s]

    while True:
        is_tidy = True
        for j in range(n-1):

            if l[j]>l[j+1]:
                l[j] = l[j]-1
                for j2 in range(j+1,n):
                    l[j2] = 9
                is_tidy = False
                break
        if is_tidy:
            break

    return ''.join([str(k) for k in l]).lstrip('0')

f_out = open(outfile, 'w')

for i in range(n):

    s = fid.readline().strip()

    sol = find_tidy(s)
    l = 'Case #%i: %s\n' % (i + 1, sol)
    f_out.write(l)
    print(sol)

f_out.close()
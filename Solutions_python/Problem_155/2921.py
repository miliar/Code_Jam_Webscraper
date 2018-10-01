'''
usage: primadonna.py [i] [o]
'''
import sys

def counter(sample):
    audience = 0
    invites = 0
    for si, am in enumerate(sample):
        if si <= audience:
            audience += int(am)
        else:
            invites += (si - audience)
            audience += (si - audience) + int(am)
    return invites

def main(fin, fout):
    f = open(fin, 'r', encoding='utf-8')
    t = int(f.readline())
    ds = []
    for i in range(0, t):
        ds.append(f.readline().rstrip().split()[1])
    f.close()
    f = open(fout, 'w', encoding='utf-8')
    for i,s in enumerate(ds, start=1):
        f.write('Case #{}: {}\n'.format(i, counter(s)))
    f.close()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print(__doc__)

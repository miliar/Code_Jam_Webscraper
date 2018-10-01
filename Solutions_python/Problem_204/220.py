import numpy as np

input_file = 'B-small-attempt0.in'
output_file = 'B.out'

with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            n, p = map(int, f.readline().split())
            reqs = map(int, f.readline().split())
            ing = np.array([sorted(map(int, f.readline().split())) for _ in range(n)])
            print reqs
            print ing
            ans = 0
            inds = np.zeros(n, dtype=int)
            # kits = [[j, 0, np.ceil(1. * ing[j][0] / (1.1 * reqs[j])), np.round(1. * ing[j][0] / (.9 * reqs[j]))] for j in range(n)]
            kits = np.array([[np.ceil(1. * ing[j][0] / (1.1 * reqs[j])), np.floor(1. * ing[j][0] / (.9 * reqs[j]))] for j in range(n)])
            # kits.sort(key=lambda x: x[2])

            while np.all(inds < p):
                # if kit then all inds += 1
                # else += 1 all < max(mins)
                min_lvl = kits[:, 0].max()
                for j in range(n):
                    while inds[j] < p and kits[j, 1] < min_lvl:
                        inds[j] += 1
                        if inds[j] >= p:
                            break
                        else:
                            kits[j] = [np.ceil(1. * ing[j][inds[j]] / (1.1 * reqs[j])), np.floor(1. * ing[j][inds[j]] / (.9 * reqs[j]))]
                            print 'new_kit', kits[j]
                print 'kits', kits
                print 'inds', inds
                if np.ceil(kits[:, 0].max()) <= np.floor(kits[:, 1].min()):
                    ans += 1
                    inds += 1
                    if np.all(inds < p):
                        for j in range(n):
                            kits[j] = [np.ceil(1. * ing[j][inds[j]] / (1.1 * reqs[j])),
                                       np.floor(1. * ing[j][inds[j]] / (.9 * reqs[j]))]


            print 'Case #{i}: {res}'.format(res=ans, i=i)
            out.write('Case #{i}: {res}\n'.format(res=ans, i=i))
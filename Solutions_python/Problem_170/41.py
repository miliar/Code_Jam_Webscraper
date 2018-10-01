from itertools import product 
#with open('input') as fin:

with open('C-small-attempt1.in') as fin, open('C-small-attempt1.out', 'w') as fout:
    T = int(fin.readline())
    for ca in range(T):
        N = int(fin.readline())
        for i in range(2):
            words = set(fin.readline().strip().split(' '))
            if i == 0:
                eng = words
            elif i == 1:
                fre = words
        sentence = []
        for i in range(N - 2):
            words = set(fin.readline().strip().split(' '))
            sentence.append(words)
        ans = 2147483647


        for s in product([0,1],repeat = N - 2):
            e = set(eng)
            f = set(fre)
            for idx,_s in enumerate(s):
                if _s == 0:
                    e |= sentence[idx]
                else:
                    f |= sentence[idx]
            _tmp = len((e & f))
            ans = min(ans,_tmp)

        print >> fout, 'Case #%d: %d' % (ca + 1 , ans)

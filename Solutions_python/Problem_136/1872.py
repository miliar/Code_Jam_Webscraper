problem  = 'B'
attemptN = 0
size     = 'large'

if size == 'small':
    filename = '%s-%s-attempt%d' % (problem, size, attemptN)
else:
    filename = '%s-%s' % (problem, size)

with open(filename+'.in', 'r') as f, open(filename+'.out', 'w') as out:
    samples = int(f.readline())
    for testN in range(samples):
        curProd = 2.0
        totTime = 0.0
        C, F, X = [float(x) for x in f.readline().split()]
        while (X-C)/curProd > X/(curProd + F):
            totTime += C/curProd
            curProd += F

        totTime += X/curProd

        out.write("Case #%d: %0.7f\n" % (testN+1, totTime))

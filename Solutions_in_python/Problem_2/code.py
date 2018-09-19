import sys

def calcular(turnaround, salidaseste, llegadaotro):
#    print turnaround, salidaseste, llegadaotro
    seste = []
    for sal in salidaseste:
        a,b = map(int, sal.split(":"))
        seste.append(a*60+b)
    seste.sort()

    lotro = []
    for llg in llegadaotro:
        a,b = map(int, llg.split(":"))
        lotro.append(a*60+b+turnaround)
    lotro.sort(reverse=True)
#    print seste, lotro

    cant = 0
    if len(lotro) > 0:
        llegado = lotro.pop()
    else:
        llegado = 9999999
    for sal in seste:
        if llegado <= sal:
            if len(lotro) > 0:
                llegado = lotro.pop()
            else:
                llegado = 9999999
        else:
            cant += 1

#    print cant
    return cant

def proc(turnaround, horasa, horasb):
    horasa = [x.split() for x in horasa]
    horasb = [x.split() for x in horasb]

    # para A
    sal = [x[0] for x in horasa]
    llg = [x[1] for x in horasb]
    resa = calcular(turnaround, sal, llg)

    # para B
    sal = [x[0] for x in horasb]
    llg = [x[1] for x in horasa]
    resb = calcular(turnaround, sal, llg)

    return (resa, resb)


archinp = open(sys.argv[1])
canttests = int(archinp.readline())

for numtest in xrange(1,canttests+1):
    turnaround = int(archinp.readline())
    canta, cantb = map(int, archinp.readline().split())
    horasa = [archinp.readline().strip() for x in xrange(canta)]
    horasb = [archinp.readline().strip() for x in xrange(cantb)]
    resa, resb = proc(turnaround, horasa, horasb)
    print "Case #%d: %d %d" % (numtest, resa, resb)

import sys
import logging

logging.basicConfig(level=logging.WARNING)

def procCase(caseLine):
    iLines = caseLine.split()

    C = int(iLines.pop(0))
    b2nb = iLines[:C]

    dB2NB = dict()

    for lb2nb in b2nb:
        b = lb2nb[:2]
        nb = lb2nb[2]
        dB2NB[''.join(sorted(b, reverse=True))] = nb
        dB2NB[''.join(sorted(b, reverse=False))] = nb
    #logging.debug('base to non-base')
    #logging.debug(dB2NB)

    iLines = iLines[C:]

    D = int(iLines.pop(0))
    dBO = list()

    bo = iLines[:D]

    for sbo in bo:
        dBO.append(set([sbo[0], sbo[1]]))

    #logging.debug('opposed')
    #logging.debug(dBO)

    iLines = iLines[D:]

    N = int(iLines.pop(0))
    sN = [c for c in iLines.pop(0)]

    curPs = list()
    curPset = set()
    restPs = sN

    while len(restPs) != 0:
        if len(restPs) == 0: break
        tc = restPs.pop(0)
        if len(curPs) == 0:
            curPs.append(tc)
            continue

        tailPair = ''.join([curPs[-1], tc])
        if tailPair in dB2NB:
            curPs.pop()
            tc = dB2NB[tailPair]
        curPs.append(tc)
        curPset = set(curPs)

        for kset in dBO:
            if kset.issubset(curPset):
                curPs = list()
                curPset = set()
                break

    logging.debug('result '+', '.join(curPs))
    return '[%s]'%(', '.join(curPs))


def main():
    iLines = file(sys.argv[1], 'r').read().strip().split('\n')
    oLines = list()
    for caseNO in range(int(iLines.pop(0).strip())):
        logging.info('Case #%i', caseNO)
        oLines.append('Case #%i: %s'%(caseNO+1, procCase(iLines.pop(0).strip())))
        logging.info('')
    file(sys.argv[1]+'.out.txt', 'w').write('\n'.join(oLines))

if __name__ == '__main__':
    main()


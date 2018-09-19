# import doctest

def fmter(s):
    return '[' + ', '.join(s) + ']'

def combiner(magicC, magicK, replC, l):
    if l[-1] + l[-2] == magicC and (l[-1] == magicK or l[-2] == magicK):
        return l[:-2] + [replC]
    return l

def neutraliser(n, mD, l):
    t = l[-1]

    for e in l[:-1]:
        if e + t == n and (e == mD or t == mD):
            return []
    return l

def resolve(s):
    """Resolve google code jam 2011

    >>> resolve('0 0 2 EA')
    '[E, A]'
    >>> resolve('1 QRI 0 4 RRQR')
    '[R, I, R]'
    >>> resolve('1 QFT 1 QF 7 FAQFDFQ')
    '[F, D, T]'
    >>> resolve('1 EEZ 1 QE 7 QEEEERA')
    '[Z, E, R, A]'
    >>> resolve('1 ASX 1 WR 10 FSSQQASEQF')
    '[F, S, S, Q, Q, X, E, Q, F]'
    """
    params = s.split()
    C = int(params[0])
    nextp = 1
    Cs = Ds = []
    magicC = 0
    magicK = ''
    replC = 0
    neutlD = 0
    neutlK = 0
    Ns = ''
    if C:
        Cs = [ord(x) for x in params[nextp]]
        magicC = Cs[0] + Cs[1]
        magicK = Cs[0]
        replC = Cs[2]
        nextp = nextp + 1
    D = int(params[nextp])
    nextp = nextp + 1
    if D:
        Ds = [ord(x) for x in params[nextp]]
        neutlD = Ds[0] + Ds[1]
        neutlK = Ds[0] # l'un ou l'autre
        nextp = nextp + 1
    N = int(params[nextp])
    nextp = nextp + 1
    if N:
        Ns = [ord(x) for x in params[nextp]]

    resp = []

    if N == 0:
        return resp
    if C == 0 and D == 0:
           return fmter([chr(x) for x in Ns])
    for elt in Ns:
        resp = resp + [elt]
        if len(resp) >= 2:
            resp = combiner(magicC, magicK, replC, resp)
            resp = neutraliser(neutlD, neutlK, resp)
    return fmter([chr(x) for x in resp])

def cas(i, s):
    print('Case #{}: {res}'.format(i, res=resolve(s)))

if __name__ == "__main__":
    N = int(input())
    tc = ['']
    for i in range(1, N + 1):
        tc = tc + [input()]
    for i in range(1, N + 1):
        cas(i, tc[i])


__author__ = 'Yongji'


def deal(data):
    s, t = data.split(' ')
    l = map(int, t)
    total = 0
    needed = 0
    for i, j in enumerate(l):
        if j != 0 and total < i:
            needed += i - total
            total += needed
        total += j
    return needed


if __name__ == '__main__':
    fp = open('A-small-attempt1.in').readlines()
    wfp = open('A-small-attempt1.out', 'w')
    for i in range(int(fp[0].strip())):
        result = deal(fp[i+1].strip())
        wfp.write('Case #%d: %s\n' % (i + 1, str(result)))

import sys

sys.setrecursionlimit(10000)

goodPairs = set([('R','G'), ('R','B'), ('R','Y'),
                 ('B','O'), ('B','R'), ('B','Y'),
                 ('Y','V'), ('Y','R'), ('Y','B'),
                 ('G','R'), ('O','B'), ('V','Y')])

def stable(n, r, o, y, g, b, v, s):
    if n == 0:
        if (s[-1],s[0]) in goodPairs: return s
        else: return None
    if s and s[-1] == 'G': 
        if r: return stable(n-1, r-1, o, y, g, b, v, s+'R')
        else: return None
    if s and s[-1] == 'O':
        if b: return stable(n-1, r, o, y, g, b-1, v, s+'B')
        else: return None
    if s and s[-1] == 'V':
        if y: return stable(n-1, r, o, y-1, g, b, v, s+'Y')
        else: return None

    # Check for invalid states so we can bail out early
    radj, badj, yadj = 0,0,0
    if s:
        if s[0] == 'R': radj += 1
        if s[-1] == 'R': radj += 1
        if s[0] == 'B': badj += 1
        if s[-1] == 'B': badj += 1
        if s[0] == 'Y': yadj += 1
        if s[-1] == 'Y': yadj += 1
    if r > b + y + g + 1 - radj: return None
    if b > r + y + o + 1 - badj: return None
    if y > r + b + v + 1 - yadj: return None
    #if o > b + badj - 1: return None
    #if g > r + radj - 1: return None
    #if v > y + yadj - 1: return None
        
    if r and (not s or s[-1] == 'B' or s[-1] == 'Y'):
        res = stable(n-1, r-1, o, y, g, b, v, s+'R')
        if res: return res
    if b and (not s or s[-1] == 'R' or s[-1] == 'Y'):
        res = stable(n-1, r, o, y, g, b-1, v, s+'B')
        if res: return res
    if y and (not s or s[-1] == 'R' or s[-1] == 'B'):
        res = stable(n-1, r, o, y-1, g, b, v, s+'Y')
        if res: return res
    if g and (not s or s[-1] == 'R'):
        res = stable(n-1, r, o, y, g-1, b, v, s+'G')
        if res: return res
    if o and (not s or s[-1] == 'B'):
        res = stable(n-1, r, o-1, y, g, b, v, s+'O')
        if res: return res
    if v and (not s or s[-1] == 'Y'):
        res = stable(n-1, r, o, y, g, b, v, s+'V')
        if res: return res
    return None

if __name__ == '__main__':
    ncases = int(raw_input())
    for case in xrange(1, ncases+1):
        n,r,o,y,g,b,v = map(int, raw_input().split())
        res = stable(n, r, o, y, g, b, v, '')
        if not res: res = 'IMPOSSIBLE'
        print 'Case #%d: %s' % (case, res)

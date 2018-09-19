fi = open('lin.txt','r')
fo = open('lout.txt','w')
n = int(fi.readline())
wx = ['XXXX','TXXX']
wo = ['OOOO','OOOT']
def state(s):    
    for i in xrange(len(s)):
        tr = ''.join(sorted(s[i]))
        tc = ''.join(sorted(zip(*s)[i]))
        if tr in wx or tc in wx:return 'X won'
        elif tr in wo or tc in wo:return 'O won'   
    d1 = ''.join(sorted([s[0][0],s[1][1],s[2][2],s[3][3]]))
    d2 = ''.join(sorted([s[0][3],s[1][2],s[2][1],s[3][0]]))
    if d1 in wx or d2 in wx:return 'X won'
    elif d1 in wo or d2 in wo:return 'O won'
    for i in xrange(len(s)):
        if '.' in s[i]:return 'Game has not completed'
    return 'Draw'
for i in xrange(n):
    board = []
    for j in range(4):board.append(list(fi.readline().strip()))
    fo.write('Case #%d: %s\n'%(i+1,state(board)))
    fi.readline()
fi.close()
fo.close()




def middle(r, y, b):

    if r > y+b or y > r+b or b > r+y:
        return "IMPOSSIBLE"
    res = ''
    letters = [[r,'R'], [y, 'Y'], [b,'B']]
    
    letters = sorted(letters)[::-1]
    res += letters[2][0]* (letters[0][1] + letters[1][1] + letters[2][1])
    letters[0][0] -= letters[2][0]
    letters[1][0] -= letters[2][0]
    res += letters[1][0]* (letters[0][1] + letters[1][1])
    letters[0][0] -= letters[1][0]
    while letters[0][0] > 0:
        idx = res.find(letters[1][1]+letters[2][1])
        res = res[0:idx+1] + letters[0][1] + res[idx+1:]
        letters[0][0] -= 1
    return res
    

def solve(n,r,o,y,g,b,v):

    bo = 0
    rg = 0
    yv = 0
    if b >= o:
        bo = o
        b -= o
    elif o > 0:
        return "IMPOSSIBLE"
    
    if y >= v:
        yv = v
        y -= v
    elif v > 0:
        return "IMPOSSIBLE"
 
    if r >= g:
        rg = g
        r -= g
    elif g > 0:
        return "IMPOSSIBLE"

    
    mid = middle(r, y, b)
    if mid == "IMPOSSIBLE":
        return mid
    sbo = bo*'BO'
    syv = yv*'YV'
    srg = rg*'RG'

    if bo > 0:
        if mid == 'B':
            return "IMPOSSIBLE"
        idx = mid.find('B')
        mid = mid[0:idx-1]+sbo+mid[idx:]
        
    if yv > 0:
        if mid == 'Y':
            return "IMPOSSIBLE"
        idx = mid.find('Y')
        mid = mid[0:idx-1]+syv+mid[idx:]
    
    if rg > 0:
        if mid == 'R':
            return "IMPOSSIBLE"
        idx = mid.find('R')
        mid = mid[0:idx]+srg+mid[idx:]
    #print mid
    return mid

    
if __name__ == "__main__":
    
    f = open("input.txt")
    lines = f.readlines()
    f.close()
    t = int(lines[0])
    i = 1
    while i <= t:
        tab = []
        tab = map(int, lines[i].strip().split(' '))
        #print tab
        res = solve(tab[0],tab[1],tab[2],tab[3],tab[4],tab[5], tab[6])
        print "Case #%d: %s" % (i, res)
        i += 1



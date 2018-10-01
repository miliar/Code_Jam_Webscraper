import scipy as sp

T = int(raw_input(''))
for t in range(T):
    N,M = map(int, raw_input('').split(' '))
    lawn = []
    for i in range(N):
        lawn.append(map(int, raw_input('').split(' ')))

    lmat = sp.array(lawn)
    # If a tile is smaller than 2 directions around it, it is bad

    lmat2 = sp.zeros((N+2,M+2))
    lmat2[1:-1,1:-1] = lmat

    maxcol = lmat.max(0).reshape(1,M).repeat(N,axis=0)
    maxrow = lmat.max(1).reshape(N,1).repeat(M,axis=1)

    above = lmat < lmat2[:-2,1:-1]
    below = lmat < lmat2[2:,1:-1]
    left  = lmat < lmat2[1:-1,:-2]
    right = lmat < lmat2[1:-1,2:]
    
    vert = above+below
    horiz = left + right

    notmaxcol = lmat < maxcol
    notmaxrow = lmat < maxrow

    if (vert * horiz + (vert * notmaxrow) + (horiz*notmaxcol) + (notmaxrow * notmaxcol)).any():
        answer = "NO"
    else:
        answer = "YES"
        

    

    print ("Case #%d:"%(t+1)), answer

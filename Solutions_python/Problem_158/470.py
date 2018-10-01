
def solve(X, R, C):
    if X>R and X>C: #line must fit in at least one dimension
        return False
    if X == 1: #trivial
        return True
    if X == 2: #only piece is a 1x2 block, it suffices that one dimension must be even
        return R%2==0 or C%2==0
    #from here on, all cases are enumerated
    if X == 3: #only 2 pieces: 1x3 and L
        #since at this point R>=X or C>=X, and R,C<=4 the only possible grids are 1x4, 2x4, 3x4, 4x4, 1x3, 2x3, 3x3 (and symmetrics)
        max_d = max(R,C)
        min_d = min(R,C)
        if max_d == 3:
            if min_d == 1:
                return False #L
            if min_d == 2:
                return True #two Ls or two lines
            if min_d == 3: #checked
                return True
        if max_d == 4:
            if min_d == 1:
                return False #L
            if min_d == 2:
                return False #nothing will fit in
            if min_d == 3:
                return True #checked
    if X == 4:
        #since at this point R>=X or C>=X, and R,C<=4 the only possible grids are 1x4, 2x4, 3x4 and 4x4 (and symmetrics)
        min_d = min(R,C)
        if min_d == 1:
            return False #Any piece that's not the line
        if min_d == 2:
            return False #Pyramid
        if min_d == 3:
            return True
        if min_d == 4:
            return True
        #both for 3 and 4, just check all 5 pieces possibly chosen by Richard:
        #2x2: OK
        #L: OK
        #pyramid: OK
        #thingie: OK
        #line: ok
        
T = int(input())
for case in range(T):
    X,R,C = list(map(int,input().split(' ')))
    print("Case #", case+1, ': ', 'GABRIEL' if solve(X,R,C) else 'RICHARD', sep='')
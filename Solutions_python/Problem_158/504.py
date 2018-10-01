# 7+ominoes can have holes => Richard instawin
# So only need to handle 1-6ominoes

# 1-omino => Gabe instawin
# 2-omino => Even Gabe instawin, Odd Richard instawin

# any-omino: if R or C < X, choose X by 1 => Richard instawin
#            if R or C >= X...
#            R*C%X != 0 => Richard win
#            force a hole => Richard win
#            otherwise => Gabe win
#            both side bounding box > other dim => Richard win

#    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
#  1 x  x  x  x                                    
#  2    x     x     x     x                        
#  3       x        x        x        x         
#  4          x           x           x           x


T = int(input())

for t in range(T):
    X, R, C = map(int, input().split())

    cells = R*C

    yes = False

    if X == 1:
        yes = True
    elif X == 2:
        if cells % 2 == 0:
            yes = True
    elif X == 3:
        if cells % 3 == 0 and cells != 3:
            yes = True
    elif X == 4:
        if cells % 4 == 0 and cells//4 > 2:
            yes = True

    if yes:
        print('Case #{}: GABRIEL'.format(t+1))
    else:
        print('Case #{}: RICHARD'.format(t+1))


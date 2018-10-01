#Name: Robin Park
#Username: robinp
#Google Code Jam Round 1B 2017

import random
import math

def isValid(arr):
    length = len(arr)
    for k in range(length):
        if arr[k%length] == arr[(k+1)%length]:
            return False
    return True

def solve(N, R, O, Y, G, B, V):

    if R > N/2 or Y > N/2 or B > N/2:
       return "IMPOSSIBLE"
    
    if R == 0:
        if Y == B:
            return "YB"*int(N/2)
    if Y == 0:
        if R == B:
            return "RB"*int(N/2)
    if B == 0:
        if R == Y:
           return "YR"*int(N/2)

    if R == Y and Y == B:
        return "RYB"*int(N/3)

    min_color = min(R, Y, B)    # recur over R, Y, B a la euclidean algorithm style
    R = R - min_color 
    Y = Y - min_color 
    B = B - min_color 

    new_N = R + Y + B
    
    #if R >= new_N/2 or Y >= new_N/2 or B >= new_N/2:
    #    return "IMPOSSIBLE"

    if R == Y and R == 0:
        if B <= min_color:
            return "BRBY"*B + "BRY"*(min_color-B)
    if B == Y and Y == 0:
        if R <= min_color:
            return "RYRB"*R + "RYB"*(min_color-R)
    if R == B and R == 0:
        if Y <= min_color:
            return "YRYB"*Y + "YRB"*(min_color-Y)


    if R == 0:
        if Y > B:
            if Y - B <= min_color:
                return "RYBY"*(Y-B) + "RBY"*(min_color-Y+B) + "BY"*B
            else:
                return "IMPOSSIBLE"
        else:
            if B - Y <= min_color:
                return "RBYB"*(B-Y) + "RYB"*(min_color-B+Y) + "YB"*Y
            else:
                return "IMPOSSIBLE"
    if Y == 0:
        if B > R:
            if B - R <= min_color:
                return "YBRB"*(B-R) + "YRB"*(min_color-B+R) + "RB"*R
            else:
                return "IMPOSSIBLE"
        else:
            if R - B <= min_color:
                return "YRBR"*(R-B) + "YBR"*(min_color-R+B) + "BR"*B
            else:
                return "IMPOSSIBLE"
    if B == 0:
        if R > Y:
            if R - Y <= min_color:
                return "BRYR"*(R-Y) + "BYR"*(min_color-R+Y) + "YR"*Y
            else:
                return "IMPOSSIBLE"
        else:
            if Y - R <= min_color:
                return "BYRY"*(Y-R) + "BRY"*(min_color-Y+R) + "RY"*R
            else:
                return "IMPOSSIBLE"

            

if __name__ == '__main__':
    with open('unicorn.in', 'r') as file, open('unicorn.out', 'w') as w:  
        T = int(file.readline().strip())
        for t in range(T):
        
            N, R, O, Y, G, B, V = map(int, file.readline().strip().split())

            
            w.write('Case #' + str(t+1) + ': ')
            w.write(solve(N, R, O, Y, G, B, V))
            w.write('\n')

print("done")

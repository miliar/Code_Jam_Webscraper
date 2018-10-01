__author__ = 'drex'

import math as m



def main():
    global gcount
    T = int(input())

    for i in range(T):
        print('Case #{0}: '.format(i+1), end='')
        row1 = list(map(int, input().split()))
        X = row1[0]
        R = row1[1]
        C = row1[2]
        tot = R*C
        
        if X == 1:
            print('GABRIEL')
            continue
 
        
        if (X == 4):
            if (R < 4 and C < 4):
                print('RICHARD')
                continue            
            if( tot == 16 or tot == 12):
                print('GABRIEL')
                continue
            else:
                print('RICHARD')
                continue
            
        if (X == 3):
            if (R < 3 and C < 3):
                print('RICHARD')
                continue  
            if( tot == 6 ):
                print('GABRIEL')
                continue
            elif tot > 6 and tot%3 == 0:
                print('GABRIEL')
                continue
            else:
                print('RICHARD')
                continue
           
            
        if (X == 2):
            if (R < 2 and C < 2):
                print('RICHARD')
                continue  
            if R%2==0 or C%2==0:
                print('GABRIEL')
                continue
            elif tot%6 == 0:
                print('GABRIEL')
                continue
            else:
                print('RICHARD')
             
            
        
        if X >= 7:
            print('RICHARD')
            continue
            

main()


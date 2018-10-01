import os
import sys
def solve(arr):
    c = 0
    card = -1
    for it in arr[0]:
        if it in arr[1]:
            c += 1
            card = it   
    if c == 1:
        return card
    elif c > 1:
        return "Bad magician!"    
    return "Volunteer cheated!" 
T = int(sys.stdin.readline().strip())
case = 1
for _ in xrange(T):
    arr = []
    for _ in xrange(2):
        ans = int(sys.stdin.readline().strip())
        row = []
        for i in xrange(1,5):
            line = sys.stdin.readline().strip()
            if  i == ans:
                row = map(int,line.split())
                
        arr.append(row)        
    print "Case #%d:" %(case), solve(arr)    
    case += 1

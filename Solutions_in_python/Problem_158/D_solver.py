
import sys
n = int(sys.stdin.readline())

for case_i in range(n):
    
    X, R, C= map(int, sys.stdin.readline().split())
    ans = ["RICHARD", "GABRIEL"]
    solution = ans[0]
    
    if X ==1:
        solution = ans[1]
    elif X ==2:
        if R*C % 2 == 0:
            solution = ans[1]
        else:
            solution = ans[0]
    elif X ==3:
        if R*C <=3 or R*C % 3 !=0:
            solution = ans[0]
        else:
            solution = ans[1]
    else:
        if R<=3 and C<=3:
            solution = ans[0]
        elif R*C in [12, 16]:
            solution = ans[1]
    
    
    print "Case #{0}: {1}".format(case_i+1, solution )
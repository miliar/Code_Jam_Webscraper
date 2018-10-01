    
import sys

T = int(sys.stdin.readline())
for case in xrange(1, T+1):
    l = map(float, sys.stdin.readline().split())
    C = l[0]
    F = l[1]
    X = l[2]
    
    #print C, F, X
    
    old_best_time = X
    best_time = X/2
    plants = 0
    plants_init = 0
    while best_time < old_best_time:
        old_best_time = best_time
        
        plants_init += C/(2+plants*F)
        plants += 1
        best_time = plants_init + X/(2+plants*F)
    
    out = "Case #"+str(case)+": "+str(old_best_time)
    print out

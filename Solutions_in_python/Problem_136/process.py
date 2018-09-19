import math

def solve(C, F, X):
    t = 0;
    v = 2;
    best_t = X/v;
    while 1:
        t += C/v;
        v += F;
#        print v
        new_t = t+X/v;
        if new_t>best_t:
            return best_t
        best_t = new_t

print solve(551.05, 62.0, 100000.0)

#f_in = open('B-large.in', 'r')
#f_out = open('B-large.out', 'w')
#
#
#T = int(f_in.readline())
#for case_id in range(T):
#    [C, F, X] = [float(x) for x in f_in.readline().strip().split()]
#    f_out.write("Case #"+str(case_id+1)+": "+str(solve(C, F, X))+"\n")
import time
from fractions import Fraction

print (time.ctime())

f_in = open('c:/temp/codejam/round1b/B-large.in')
f_out = open('c:/temp/codejam/round1b/B-large.out','w')

C = int(f_in.readline())
for case in range(1,C+1):
    N, K, B, T = [int(x) for x in f_in.readline().split()]
    init_places = [int(x) for x in f_in.readline().split()]
    velocities = [int(v) for v in f_in.readline().split()]
    is_able_to_reach = [None]*N
    for i in range(N):
        time_to_reach = Fraction(B - init_places[i] , velocities[i])
        if time_to_reach <= T:
            is_able_to_reach[i] = True
        else:
            is_able_to_reach[i] = False

    n_can_reach = is_able_to_reach.count (True)
    
    if n_can_reach >= K:
        total_must_skip = 0
        is_able_to_reach.reverse()
        for i in range(K):
            must_skip = is_able_to_reach.index(True)
            total_must_skip += must_skip
            del is_able_to_reach[must_skip]
        res = total_must_skip
    else:
        res = 'IMPOSSIBLE'
    
    f_out.write('Case #' + str(case) + ': ' + str(res) + '\n')

f_out.close()
f_in.close()

print (time.ctime())


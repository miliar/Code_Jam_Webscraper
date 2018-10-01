import fileinput 
import sys

stdin = fileinput.input()

def lb_on_how_long_it_will_take_horse_to_reach_D(D, K, S):
    return (D - K) / float(S)

def do_case(D, N, horses):
    max_time = max([ lb_on_how_long_it_will_take_horse_to_reach_D(D, K, S) for (K, S) in horses])
    return D / max_time
        
T = int(next(stdin))
print "T:", T

for case_num in range(1, T+1):
    case_input = next(stdin)
    D, N = case_input.split(' ')
    D, N = int(D), int(N)
    print "D:", D, "N:", N
    horses = []
    for i in range(N):
        case_input = next(stdin)
        K, S = case_input.split(' ')
        K, S = int(K), int(S)
        horses.append((K, S))
    print "horses: ", horses
    x = do_case(D, N, horses)
    print "Case #{}: {}".format(case_num, x)
    sys.stdout.flush()


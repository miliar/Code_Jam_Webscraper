import math
def solve():
    N, K = map(int, raw_input().split())
    U = float(raw_input())
    P = map(float, raw_input().split())
    P = sorted(P)

    
    def calc(PP):
        if 0 in PP:
            return 0
        PPP = map(math.log, PP)
        ans = math.exp(sum(PPP))
        return ans

    ansPrev = calc(P)
    while U > 0:
        mi = min(P)
        end = 0
        while end < len(P) and P[end] <= mi:
            end += 1
        if end < len(P):
            target = P[end]
        else:
            target = 1

        if U >= (target - mi)*end:
            inc = target - mi
            U -= (target - mi) * end
            for i in range(end):
                P[i] = target
        else:
            inc = U/end
            U = 0
            for i in range(end):
                P[i] += inc
        
        ans = calc(P)
        if ans <= ansPrev:
            break
        else:
            ansPrev = ans
        #print inc, U, target, mi, end

        #print P


    #print P
    ans = calc(P)
    return ans









T = int(raw_input())
for t in range(1, T+1):
    print "Case #{}: {}".format(t, solve())

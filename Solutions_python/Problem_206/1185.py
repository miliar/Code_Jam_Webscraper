'''
def solve(horses, D):
    if len(horses) == 1:
        s2, p2 = horses[0]
        return s2*D / (D-p2)
    h1, h2 = sorted(horses,reverse=True) # small
    p1, s1 = h1
    p2, s2 = h2
    if s1 > s2: 
        return s2*D / (D-p2)
    else:
        t1 = (s2-s1)/(p1-p2)
        d_ = p2 + s2*t1
        lim1 = d_*s2/(d_-p2)
        lim2 = D*s1/(D-p1)
        return min(lim1, lim2)
'''
def solve(horses, D):
    maxt = 0
    for p, s in horses:
        #print maxt, p, s
        maxt = max(maxt, (D-p)/s)
    return D/maxt

t=input()

for i in range(t):
    D, N = map(float, raw_input().strip().split())
    horses = []
    for j in range(int(N)):
        horses.append(map(float, raw_input().strip().split()))
    print "Case #{}: {}".format(i+1,solve(horses, D))

# Readin file
f = open('B-small-attempt1.in', 'r')
f2 = open('output.txt', 'w+')
N = int(f.readline())

def totalTime (nfarms, C, F, X):
    cps = 2
    t = 0
    for i in range(nfarms):
        t += C/cps
        cps += F
    t += X/cps
    return t  
 
def optimize (C, F, X):
    t_best = totalTime(0, C, F ,X)
    nfarms = 1
    while True:
        t_new = totalTime(nfarms, C, F ,X)
        if (t_new < t_best):
            nfarms+=1
            t_best = t_new
        else: break
    return t_best
        

# Loop through cases
for n in range(N):
    [C, F, X] = [float(i) for i in f.readline().split()]
    t_best = optimize(C,F,X)
    f2.write('Case #' + str(n+1)+': '+str(t_best)+'\n')

f.close()
f2.close()

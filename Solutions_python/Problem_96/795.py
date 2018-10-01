from math import *

f = open('B-small-attempt0.in', 'r')
a = open('out.txt', 'w')

# returns non-surprising set of scores given n
def get_scores(n):
    if math.ceil(n/3.)==math.floor(n/3.):
        return 3*[n/3.]
    if n/3.-math.floor(n/3.)>.5:
        return [math.ceil(n/3.),math.ceil(n/3.), math.floor(n/3.)]
    return [math.ceil(n/3.),math.floor(n/3.),math.floor(n/3.)]

for i in range(int(f.readline().strip())):
    line = [int(x) for x in f.readline().strip().split()]
    num = line[0]
    num_supr = line[1]
    p = line[2]
    scores = sorted(line[3:], reverse=True)
    result = 0
    for score in scores:
        judges = get_scores(score)
        if max(judges) >= p:
            result += 1
            continue
        if num_supr > 0:
            m = max(judges)
            judges.remove(m)
            if max(judges) == m and m+1>=p and m-1>0:
                result += 1
                num_supr -= 1
    a.write('Case #' + str(i+1) + ": " + str(result) + "\n")
    print 'Case #' + str(i+1) + ": " + str(result)
    
f.close()
a.close()

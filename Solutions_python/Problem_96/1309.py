# Dancing With the Googlers

import sys

def getline():
    return sys.stdin.readline().strip()

   
def run(data):
    s = data[1]
    p = data[2]
    data = data[3:]
    
    scores = list()
    for t in data:
        score = list()
        r = t % 3
        z = t / 3
        if r == 0:
            if z >= p:
                score.append([z, z, z])
            if z+1 >= p and z-1>=0:
                score.append([z-1, z, z+1])
        if r == 1:
            if z+1 >= p:
                score.append([z, z, z+1])
        if r == 2:
            if z+1 >= p:
                score.append([z, z+1, z+1])
            if z+2 >= p:
                score.append([z, z, z+2])
                
        scores.append(score)
    
    cnt = 0
    remain = list()
    for score in scores:
        if len(score) == 1:
            if score[0][2]-score[0][0]>=2:
                if s>0:
                    s -= 1
                    cnt += 1
            else:
                cnt += 1
                
        if len(score) == 2:
            cnt += 1
    
    # print scores
    return cnt

n = int(getline())

for id in range(1, n+1):
    print 'Case #%d:' % id,
    
    print run(map(int, getline().split(' ')))
    

'''
Created on Apr 14, 2012

@author: shelajev
'''

def solve(N, s, p, scores):
    ans = 0
    for x in scores:
        if x >= 3*p - 2:
            ans += 1
        elif x < 2:
            continue
        elif x >= 3*p - 4 and s > 0:
            ans += 1
            s -= 1
    return ans
        

if __name__ == '__main__':
    attempt = 1
    T = 1
#    filename = 'B-small-attempt%s.in' % attempt
    filename = 'B-large.in'
    output = open(filename + '.out', 'w')
#    filename = 'input-B.sample'
    for line in file(filename).readlines():
        if ' ' not in line:
            continue
        line = line.rstrip().split()
        N = int(line[0])
        s = int(line[1])
        p = int(line[2])
        scores = [0]*N
        for x in range(N):
            scores[x] = int(line[x+3])
        
        line = 'Case #%s: %s' % (T, solve(N, s, p, scores))
        print line
        output.write('%s\n' % line)
        
        T+=1
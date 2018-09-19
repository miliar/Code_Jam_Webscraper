'''
Created on 2010/05/09

@author: banana
'''

if __name__ == '__main__':
    pass


def furui(a, b):
    if  a > b :
        g = a;
        l = b;

    else :
        g = b;
        l = a;

    while  g > 0 :
        g -= l;

    if g == 0 :
        return l;

    else :
        g += l;
        return furui(l, g);



fp = open("B-large.in", "r")

lines = fp.readlines()

C = int(lines[0])

fpout = open("B-large.txt", "w")

for c in range(1, C+1):
    N = int(lines[c].split()[0])
    t = [0 for x in range(N)]
    for i in range(N):
        t[i] = int(lines[c].split()[i+1])
    
    
    gcd = [0 for x in range(N)]
    gcd_old = [0 for x in range(N)]
    
    #sort
    t = list(set(t))
    t.sort()
    t.reverse()
    
    N = len(t)
    
    for i in range(N-1):
        gcd[i] = t[i] - t[i+1];
    
    for i in range(N-2):
        for j in range(N-1):
            gcd_old[j] = gcd[j];
        for j in range(N-2-i):
            gcd[j] = furui(gcd_old[j], gcd_old[j+1]);
    
    ans = 0
    if t[N-1] % gcd[0] == 0 :
        ans = 0;
    
    else :
        ans = gcd[0] - (t[N-1] % gcd[0]);
    
    fpout.write("Case #%d: %d\n"%(c, ans))
    print "Case #%d: %d\n"%(c, ans)

fpout.close()
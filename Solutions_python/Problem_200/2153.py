def checkTidy(n):
    t = str(n)
    if len(t) == 1:
        return True  
    for a in range(len(str(t))):
        if a+1 == len(str(t))-1 and t[a] <= t[a+1]:
            return True
        elif t[a] > t[a+1]:
            return False        

def tidy(n):
    while(checkTidy(n) == False):
        s = str(n)
        a = 0
        b = 1
        while b < len(s):
            if s[a] > s[b]:
                n = n - (int(s[b:]) + 1)
                #print n
                break                                
            a += 1
            b += 1

    return n

f = open('B-large.in', 'r')
g = open('B-large.out', 'w')
t_c = int(f.readline().strip())
i = 1

while i <= t_c:
    num = int(f.readline().strip())
    g.write("Case #"+str(i)+': '+str(tidy(num))+'\n')
    i += 1
g.close()


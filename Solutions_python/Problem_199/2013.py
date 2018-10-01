def flip(c):
    if c == '+':
        return '-'
    else:
        return '+'

f = open('A-large.in', 'r')
g = open('A-large.out', 'w')
C = int(f.readline().strip())
i = 1
w = 0

while i <= C:
    flag = True
    line = f.readline().strip().split()
    pan = list(line[0])

    k = int(line[len(line)-1])
    for a in range(len(pan)):
        if pan[a] == '-' and a+k <= len(pan):
            w += 1
            for j in range(k):
                pan[a+j] = flip(pan[a+j])
        elif pan[a] == '-' and a+k > len(pan):
            g.write("Case #"+str(i)+': '+'IMPOSSIBLE'+'\n')
            flag = False
            break
    if flag == True:
        g.write("Case #"+str(i)+': '+str(w)+'\n')    
    i += 1    
    w = 0
    

g.close()    
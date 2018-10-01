


def flip(s, p, i):
    
    for j in range(p):
        if s[i+j] == '+':
            s[i+j] = '-'
        else:
            s[i+j] = '+'
        


file = open('B-large.in', 'r')
ofile = open('output.txt', 'w')
a = file.read()
file.close()
b = a.split('\n')

cases = b[0]
for i in range(1, len(b)):
    if b[i] == '':
        continue
    s = b[i]
    l = len(s)
    n = int(s)
    ind = 1
    while ind > 0:
        ind = -1
        for k in range(l):
            j = l-k-1
            c = (n % 10**(j+1))//(10**j)
            d = (n % 10**(j+2))//(10**(j+1))
            if d > c:
                ind = k-1
                break
        if ind >-1:
            if ind+1 < len(s):
                n -= (10**(l-ind-1))
            for k in range(ind+1, l):
                j = l-k-1
                c = (n % 10**(j+1))//(10**j) 
                n -= c*(10**j)
                n += 9*(10**j)
   
    
        
    ofile.write('Case #'+str(i)+': ' + str(n)+'\n')
ofile.close()
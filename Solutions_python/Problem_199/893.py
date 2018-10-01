def flip(s,k,j):
    for i in range(0,k):
        if j+i >= len(s):
            return False
        if s[j+i] == '-':
            s[j+i] = '+'
        else:
            s[j+i] = '-'
    return True
    
fin = open('./A-large.in','r')
fout = open('./output.txt','w')
t = int(fin.readline())
for i in range(0,t):
    s,k = fin.readline().split()
    k = int(k)
    s = list(s)
    noFlip = 0
    for j in range(0,len(s)):
        if s[j] == '-':
            if flip(s,k,j) == False:
                noFlip = -1
                break
            noFlip = noFlip+1
    if noFlip == -1:
        fout.write('Case #{}: IMPOSSIBLE\n'.format(i+1))
    else:
        fout.write('Case #{}: {}\n'.format(i+1,noFlip))
fin.close()
fout.close()

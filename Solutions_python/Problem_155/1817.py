def ovation(m, inStr):
    totes = 0
    needed = 0
    for i in range(m+1):
        if totes >= i:
            totes += int(inStr[i])
        else:
            while(totes<i):
                totes += 1
                needed += 1
            totes += int(inStr[i])
            
    return needed
        

fin = open('A-large.in','r')
fout = open('output.txt','w')

T = int(fin.readline())
print T

for i in range(T):
    temp = fin.readline().split(' ')
    ans = ovation(int(temp[0]), temp[1])
    fout.write("Case #%d: %d\n"%(i+1, ans))

fin.close()
fout.close()
infile = open('D-large.in','r')
outfile = open('3out.txt','w')
total = int(infile.readline())
for t in range(total):
    num = int(infile.readline())
    nao=sorted(infile.readline().split(' '))
    ken=sorted(infile.readline().split(' '))
    nao.append('0')
    ken.append('0')
    i = 0
    j = 0
    s1 = 0
##    print(nao)
##    print(ken)
    while j<num:
        while nao[i]>ken[j] and j<num:
            j+=1
            s1+=1
        i+=1
        j+=1
   
    i = 0
    j1 = 0
    j2 = num-1
    s2=0
    while j1<=j2:
        if nao[i]<ken[j1]:
            j2-=1
        else:
            j1+=1
            s2+=1
        i+=1
    outfile.write('Case #'+str(t+1)+': '+str(s2)+' '+str(s1)+'\n')
        
infile.close()
outfile.close()

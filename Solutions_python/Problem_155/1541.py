if __name__ == '__main__':
    f = file('A-large.in')
    g=file('output.txt','w')
    line=f.readline()
    T=int(line)
    for k in range(T):
        line=f.readline()
        temp=line.split(" ")
        Smax=temp[0]
        minf=0
        count=0
        for i in range(len(temp[1])-1):
            if count<i:
                minf+=i-count
                count=i
            count+=int(temp[1][i])
        ans="Case #"+str(k+1)+': '+str(minf)+'\n'
        g.write(ans)
    f.close()
    g.close()
def check(l):
    t=0
    p=0
    n=int(l[0])
    s1=l[n]
    n2=int(l[5])
    s2=l[n2+5]
    for i in s1:
        for j in range(4):
            if(i==s2[j]):
                t+=1
                p=s2[j]
    if(t>1):
        return "Bad magician!"
    elif(t==1):
        return p
    elif(t==0):
        return "Volunteer cheated!"
def test():
    data = open('aaa.txt','r')
    data2= open('aaa2.txt','w')
    k= data.read()
    line=k.split('\n')
    l=1
    c=[]
    for i in range(int(line[0])):
            n=[line[l],line[l+1].split(' '),line[l+2].split(' '),line[l+3].split(' '),line[l+4].split(' '),line[l+5],line[l+6].split(' '),line[l+7].split(' '),line[l+8].split(' '),line[l+9].split(' ')]
            c.append(n)
            l+=10
    for j in range(int(line[0])):
        data2.write("Case #%d: %s\n" % (j+1,check(c[j])))
    data.close
    data2.close
test()

def commonstart():
    fin=open(r'C:\Users\Administrator\Desktop\google jam\2014\Part Elf\A-large.in','r')
    fout=open(r'C:\Users\Administrator\Desktop\google jam\2014\Part Elf\A.out','w')
    return fin,fout
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

fin,fout=commonstart()
num=int(fin.readline())
maxy=2**40
for line in range(0,num):
    x,y=map(int,fin.readline().split('/'))
    gong=gcd(x,y)
    x=x//gong
    y=y//gong
    if maxy%y!=0:
        print('Case #%s: impossible'%(line+1),file=fout)
        continue
    for each in range(1,41):
        if x/y>=1/(2**each):
            result=each
            break
    print('Case #%s: %s'%(line+1,result),file=fout)
fin.close()
fout.close()
    
        

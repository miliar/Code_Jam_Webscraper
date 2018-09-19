# Problem C. Recycled Numbers #

def recycled(n,m):
    for letter in n:
        if letter not in m: return 0
    for letter in m:
        if letter not in n: return 0
    l=len(n)
    if l==2:
        if n==m[::-1]:
            return 1
        return 0
    else:
        for i in range(1,l):
            if n[l-i:]+n[:l-i]==m:
                return 1
    return 0

T = int(raw_input())
File = open('Bout.txt','w')

for i in range(1,T+1):
    c=0
    File.write("Case #"+str(i)+": ")
    a = [int(x) for x in raw_input().split()]
    if a<10:
        File.write("0")
    else:
        A,B=int(a[0]),int(a[1])
        for j in range(B,A-1,-1):
            for k in range(A,j):
                c+=recycled(str(j),str(k))
    File.write(str(c))
    if i==T:
        break
    File.write('\n')
File.close()

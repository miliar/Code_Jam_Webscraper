import sys
fout = open("answersClarge1.out", "w")
fin = open("C-large-1.in", "r")
def is_palindrome(x):
    if(x%10==0):
        return False
    L=[]
    while(x!=0):
        L.append(x%10)
        x=x//10
    n =len(L)
    for i in range(int(n/2)+1):
        if(L[i]!=L[n-1-i]):
            return False
    return True

def reverse(s):
    n=len(s)
    y=list(s)
    s=""
    for i in range(0,int(n/2)):
        a=y[i]
        y[i]=y[n-1-i]
        y[n-1-i]=a
    for i in range(n):
        s+=y[i]
    return s

Fair=[1,4,9]
for i in range(1,999):
    n=len(str(i))
    s=reverse(str(i))
    j=int(s)
    num=i*(10**n) + j
    if(is_palindrome(num*num)):
        Fair.append(num*num)

for i in range(1,999):
    n=len(str(i))
    s=reverse(str(i))
    j=int(s)
    for k in range(0,10):
        num=i*(10**(n+1)) + j + k*(10**n)
        if(is_palindrome(num*num)):
            Fair.append(num*num)

T=int(fin.readline())
results=[]
for t in range(T):
    result=0
    A,B = (fin.readline().split())
    A=int(A)
    B=int(B)
    for item in Fair:
        if(item>=A and item<=B):
            result+=1
    results.append(result)

for t in range(T):
    fout.write("Case #")
    fout.write(str(t+1))
    fout.write(": ")
    fout.write(str(results[t]))
    fout.write("\n")
fout.close()

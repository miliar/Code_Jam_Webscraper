import math

# Input is integer n and integer k not exceeding n
# Output is [e,[a,b], p] where e is the largest exponent such that 2^e does not exceed k,
# p is the largest part available after 2^e iterations and a is the number of parts of size p
# while b is the number of parts of size p-1

def Num_Parts(n,k):
    e=math.floor(math.log2(k))
    m=n
    A=[1,0]
    for i in range(e):
        B=[0,0]
        for j in range(2):
            if (m-j-1)/2==math.floor(m/2):
                B[0]+=2*A[j]
            else:
                if (m-j-1)/2==math.floor(m/2)-1:
                    B[1]+=2*A[j]
                else:
                    B[0]+=A[j]
                    B[1]+=A[j]
        A=B
#        print(A)
        m=math.floor(m/2)
#        print(m)
    return [e,A,math.floor(n/(2**e))]
'''
# Sample test
n1=74
k1=25
print(Num_Parts(n1,k1))
n2=74
k2=64
print(Num_Parts(n2,k2))

n=74
for k in range(1,n+1):
    print(Num_Parts(n,k) )
'''
# Input is number of stalls n and number of visitors k
# Output is [a,b] where a=max(L_S,R_S) and b=min(L_S,R_S) for the kth visitor

def Bathroom(n,k):
    B=Num_Parts(n,k)
    m=B[2]
    if k-(2**B[0]-1)<=B[1][0]:
        return [math.floor( (m-1)/2),m-1-math.floor( (m-1)/2)]
    else:
        return [math.floor( (m-2)/2),m-2-math.floor( (m-2)/2)]
'''
n=53
for k in range(1,n+1):
    print(k,Bathroom(n,k))
n=16
for k in range(1,n+1):
    print(k,Bathroom(n,k))
'''

f=open('C-small-2-attempt0.in','r')
g=open('Bathroom_stalls_small2_output.txt','w')
t=int(f.readline())
for i in range(t):
    a1,a2=f.readline().split(" ")
    n=int(a1)
    k=int(a2)
    A=Bathroom(n,k)
    g.write('Case #{0}: {1} {2}\n'.format(i+1,A[1],A[0]) )
g.close()



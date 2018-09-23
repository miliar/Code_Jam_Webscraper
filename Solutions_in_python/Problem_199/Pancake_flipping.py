# Input is single string s of + and -
# Output is list of length the number of symbols '+' and '-' written in order
def Pancake(s):
    A=[]
    for i in range(len(s)):
        A.append(s[i])
    return A
'''
#Sample test
s="+---+++----+-+-+"
A=Pancake(s)
print(A)
'''

# Input is list of pancake states (with + or -) A
# Output is true if all states are "+" and false otherwise
def Is_Happy(A):
    for i in range(len(A)):
        if A[i]=='-':
            return False
    return True

# Input is list of pancake states (with + or -) A, width of pancake flipper k and position m
# Output is a new list of pancake states (with + or -) B
def Flip(A,k,m):
    B=A[0:m]
    for i in range(m,m+k):
        if A[i]=='+':
            B.append('-')
        else:
            B.append('+')
    C=A[m+k:]
    B.extend(C)
    return B
'''
#Sample test
A=['+','+','+','-','+','-','-','-','+','-','+']
k=3
m=4
B=Flip(A,k,m)
print(B)
'''

# Input is list of pancake states (with + or -) A and width of pancake flipper k
# Output is either IMPOSSIBLE or the smallest number of flips
def Happy(A,k):
    B=A
    count=0
    for m in range(len(A)-(k-1)):
        if B[m]=='-':
            B=Flip(B,k,m)
            count+=1
#            print(B)
    if Is_Happy(B)==False:
        return "IMPOSSIBLE"
    else:
        return count
'''
#Sample test
s='+---+++----+-+-+'
k=3
A=Pancake(s)
print(Happy(A,k))
k=2
print(Happy(A,k))
'''

f=open('A-large.in','r')
g=open('Pancakes_large_output.txt','w')
t=int(f.readline())
for i in range(t):
    a1,a2=f.readline().split(" ")
    s=str(a1)
    k=int(a2)
#    print (s," ",k)
    A=Pancake(s)
    g.write('Case #{0}: {1}\n'.format(i+1,Happy(A,k) ) )
g.close()
    

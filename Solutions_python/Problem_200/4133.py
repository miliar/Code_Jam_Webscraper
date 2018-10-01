def main(s):
    T=True
    i=0
    while T and i<len(s)-1:
        if s[i]>s[i+1] :
            T=False
        else :
            i= i+1
    return T
T=int(input())
for i in range(T):
    N=input()
    nn=int(N)
    while nn>0 :
        if main(str(nn)) :
            break
        else :
            nn= nn-1
    print"Case #"+str(i+1)+": "+str(nn)
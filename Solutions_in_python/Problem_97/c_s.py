def flip(num):
    d = str(num) ; u = len(d)-1 ; w = -1
    k = set({})
    for i in range(len(d)-1):
        s = str(num)
        r = s[w:]+s[:u]
        w -= 1 ; u -= 1
        k.add(int(r))   
    #print k
    return k     
        
def Solve(A,B):
    n,f = range(A,B),0   
    for t in range(len(n)):
        K = flip(n[t]) ; K = list(K) 
        for j in range(len(K)):
            if K[j] > n[t] and K[j]<=B:# and str(K[j])[-1] != '0':
                f += 1
        t += 1
    return f
                
if __name__ == "__main__":
    f = open("C-small-attempt0.in")
    outfile = open('c_small.txt', 'a')
    T = int(f.readline())
    for i in range(1,T+1):
        q = f.readline().split()
        A = int(q[0])
        B = int(q[1])
        outfile.write("Case #%d: %d\n" % (i,Solve(A,B)))    
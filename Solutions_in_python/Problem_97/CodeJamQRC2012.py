c, C = 0, int(input())
while c != C:
    c += 1

    A, B = input().split()
    L = len(A)
    
    a = len(set(  (n,n[i:]+n[:i])
                for n in map(str,range(int(A),int(B)+1))
                for i in range(1,L)
                if n<n[i:]+n[:i]<=B
                ))
    print("Case #%d:" % c, a)
            

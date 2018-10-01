def solve(s,n):
    
    L=len(s)
    consonants=list("bcdfghjklmnpqrstvwxyz")
        # apply for n and recurse from n to L
        
    super=0
    for x in range(n,L+1):
        main=0
        for i in range(0,(L-x)+1):# +1 for inclusive iteration
        
            
            for j in range(i,i+1+x-n):
                c=0
                for k in range(0,n):
                    if s[j+k] in consonants :
                        c=c+1
                if (c==n) : 
                    main=main+1
                    break;
            
        super=super+main
    return super
    
f=open("output-consonants.txt","w")   
T=int(input("Testcases"))
for t in range(1,T+1):
    line=input()
    line.strip()
    line=line.split()
    print ("Case #"+str(t)+": "+str(solve(line[0],int(line[1]))))
    f.write("Case #"+str(t)+": "+str(solve(line[0],int(line[1])))+"\n")
f.close() 


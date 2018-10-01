f=open('A-small-attempt.in')
noi=int(f.readline().rstrip('\r\n'))
i=1
alp=['a','y','o','e','z','q','j','s','i','r','d','p','b','c','k','h','w','f','m','v','n','t','g','l','u','x']
rep=['y','a','k','o','q','z','u','n','d','t','s','r','h','e','i','x','f','c','l','p','b','w','v','g','j','m']
sol=[ [] for _ in range(noi)]
while i<=noi:
    lin=f.readline().rstrip('\r\n')
    lin=list(lin)
    for iny,x in enumerate(lin):
        try:
            ind=alp.index(x)
            sol[i-1]+=rep[ind]
            
        except ValueError:
            sol[i-1]+=' '          
  
    i+=1
ou=open('jam.out','w')    
for u,x in enumerate(sol):
    print("Case #%s: "%(u+1)+ "".join(x),file=ou)
ou.close()
f.close()

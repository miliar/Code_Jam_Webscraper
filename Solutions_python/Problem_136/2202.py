f = open('B-large.in')
iter = int(f.readline())
for i in range(iter):
    money = 0.
    segundos = 0.
    ganancia = 2.
    row = f.readline().strip().split()
    #print row
    C = float(row[0])
    F = float(row[1])
    X = float(row[2])
    while(money<X):
        if(C+money>=X):
            segundos+=float(X-money)/ganancia
            money=X
        else:
            if((X-money)/(ganancia+F) < (X-money-C)*1./ganancia):
                segundos+=C/ganancia
                ganancia+=F
            else:
                segundos+=float(X-money)/ganancia
                money=X
    print "Case #"+str(i+1)+":", segundos
                
    

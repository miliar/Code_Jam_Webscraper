in_file = open("B-small-attempt0.in","r")
T = in_file.readline()
T = int(T)

out_file = open("B-small-attempt0.out","w")

## CICLO GENERALE DEL PROGRAMMA
for i in range(T):

    tidy = False
    N = in_file.readline()
    N = N[0:len(N)-1]
    print(N)
    
    ## CICLO DI CONTROLLO PER CIASCUN NUMERO
    while tidy == False:

        if len(N) == 1:
            out_file.write("Case #"+str(i+1)+": "+str(N)+"\n")
            tidy = True
        else:
            for j in range(len(N)-1):
                if int(N[j]) <= int(N[j+1]):
                    tidy = True
                else:
                    tidy = False
                    break
            if tidy == True:
                out_file.write("Case #"+str(i+1)+": "+str(N)+"\n")
            else:
                N = int(N)
                N = N - 1
                N = str(N)

in_file.close()
out_file.close()           
            
        
                
        

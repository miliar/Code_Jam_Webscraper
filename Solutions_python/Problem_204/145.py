T = int(input())
for i in range(T):
    res = "Case #{0}: ".format(i+1)
    N, P = input().split()
    N, P = int(N), int(P)

    
    
    # Grams of the ith ingredient
    grams = []
    for l in input().split():
        grams.append(int(l))

    packsGrams = []        
    for n in range(N):
        packsGrams.append([])
        for x in input().split():
            packsGrams[n].append(int(x))
        packsGrams[n].sort(reverse=True)
    
    rendimento = []
    for n in range(N):
        rendimento.append([])
        for p in range(P):
            rendimento[n].append(packsGrams[n][p] / grams[n])
        
    
        
    kits = 0
    max = 1
    
    while (max > 0 and P>0):
    
        max = int(rendimento[0][0]/0.9)+1
        for n in range(0,N):
            if rendimento[n][0] < 0.9*max:
                max = int(rendimento[n][0]/0.9)
                
        pi = [0] * N # package index
        
        for n in range(N):
            while (pi[n] < P and (rendimento[n][pi[n]] > 1.1*max or rendimento[n][pi[n]] < 0.9*max)):
                pi[n] += 1
                if (pi[n] < P and rendimento[n][pi[n]] < 0.9*max):
                    max -= 1
                    n = 0 #restart
                    
            if (pi[n] >= P):
                break
        
        for n in range(N):
            if (pi[n] >= P):
                max = 0
                break
        if (max > 0):
            for n in range(N):
                rendimento[n][pi[n]] = 0
                rendimento[n].sort(reverse=True)
            P -= 1
            kits += 1
    
    print(res + str(kits))
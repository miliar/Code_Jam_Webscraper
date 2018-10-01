fileout = open('A-large.out',"w")

with open('A-large.in') as file:
    T = int(file.readline())
    
    for case in range(1, T + 1): 
        
        [S_in, k_in] = file.readline().split()
        S = list(S_in)
        k = int(k_in)
      
        cakes = ['-', '+']
        n = 0

        for cake in range(len(S) - k + 1):
            if S[cake] == '-':
                n += 1
                for f in range(k):
                    S[cake + f] = list(set(cakes).difference(set(S[cake + f])))[0]

        if S[-1*k :] == ['+']*k:
            fileout.write("Case #" + str(case) + ": " + str(n) + "\n")
        else:
            fileout.write("Case #" + str(case) + ": IMPOSSIBLE\n")
    
fileout.close()

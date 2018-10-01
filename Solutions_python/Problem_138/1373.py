#getting data
data = input ()
data = data.split('\n')
cases = int(data[0])
data = data [1:]

for c in range(0, cases):
    N = int(data[c*3])
    Naomi = data[c*3 + 1].split()
    Naomi.sort()
    CNaomi = Naomi.copy()
    Ken = data[c*3 + 2].split()
    Ken.sort()
    CKen = Ken.copy()
    #War game
    Wpoints = 0
    while len(Naomi) > 0:
        for k in range(0,len(Ken)):
            found = False
            if float(Naomi[0]) < float (Ken[k]):
                found = True
                index = k
                break
        Naomi.remove(Naomi[0])
        if found:
            Ken.remove(Ken[index])
        else:
            Ken.remove(Ken[0])
            Wpoints +=1
        
    #War cheat game
    Cpoints = 0
    while len(CNaomi) > 0 and float(CNaomi[0]) < float(CKen[0]):
        CNaomi.remove(CNaomi[0])
        CKen = CKen[0:(len(CKen)-1)]
    while len(CNaomi) > 0:
        if float(CNaomi[0]) > float(CKen[0]):
            Cpoints +=1
            CNaomi.remove(CNaomi[0])
            CKen.remove(CKen[0])
        else:
            CNaomi.remove(CNaomi[0])
            CKen = CKen[0:(len(CKen)-1)]
    print('Case #' + str(c+1) + ": " + str(Cpoints) + ' ' + str(Wpoints))
        

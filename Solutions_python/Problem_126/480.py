vowels = {'a','e','i','o','u'}

def nvalue(mot,lmot,n):
    total = 0
    i0 = 0
    jalon = 0
    test = True
    while i0 <= lmot-n:
        for k in range(i0,i0+n):
            if mot[k] in vowels:
                i0 = k + 1
                test = False
                break
        if test:
            total += (i0-jalon+1) * (lmot-i0-n+1)
            jalon = i0+1
            i0 += 1

        else:
            test = True
    return total



def resultats(fichier):
    f = open('{}.in'.format(fichier),'r')
    res = open('{}.out'.format(fichier),'w')
    T = int(f.readline())
    for k in range(1,T+1):
        s = f.readline().split()
        res.write('Case #{}: {}\n'.format(k,nvalue(s[0],len(s[0]),int(s[1]))))


resultats('Consonants-small-attempt0')
        

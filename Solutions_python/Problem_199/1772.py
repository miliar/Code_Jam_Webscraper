def lire(path) :
    test = open(path, "r")
    liste = []
    long = int(test.readline())
    for c in test.readlines():
        ligne = c.rstrip()
        liste.append(list(ligne.split()))
    test.close()
    return liste

def decomp(mot):
    li = []
    for c in mot :
        li.append(c)
    return(li)

def comp(x):
    if x =="+" :
        return "-"
    else :
        return "+"
    
def inv(fin, ch, larg):
    for i in range(larg):
        ch[fin-i] = comp(ch[fin-i])
    return ch
def bon(ch):
    for c in ch:
        if c =="-":
            return False
    return True

def nb_retour(mot, larg):
    larg = int(larg)
    ch = decomp(mot)
    compt =0
    n = len(ch)
    for i in range(len(ch)) :
        if ch[n-1-i] != "+" and (n-1-i) >= larg -1:
            ch = inv(n-1-i, ch, larg)
 #           print(ch)
            compt+=1
    if bon(ch):
        return compt
    else :
        return "IMPOSSIBLE"

def main():
    liste = lire("A-large.in.txt")
 #   print(liste)
    rep = open("pancakes_A_large_0", "w")
    cas = 1
    for m in liste :
        rep.write("Case #" + str(cas)+": " + str(nb_retour(m[0],m[1]))+"\n")
        cas+=1

    rep.close()
    

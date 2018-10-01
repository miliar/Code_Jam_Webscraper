if __name__ == "__main__":
    with open("B-large.in","r") as f:
        sortie = open("sortie.txt","w")
        nbLigne = 0
        for ligne in f:
            if nbLigne != 0:
                liste = ligne.split()
                i = 0
                for c in liste:
                    liste[i] = int(c)
                    i += 1
                N = liste[0]
                S = liste[1]
                P = liste[2]
                i = 3
                res = 0
                normale = P + P + P - 2
                surprenant = P + P + P - 4
                if P == 1:
                    surprenant = 1
                while i < len(liste):
                    if liste[i] >= normale:
                        res += 1
                    elif (S > 0) and (liste[i] >= surprenant):
                        res += 1
                        S -= 1
                    i += 1
                print("Case #{0}: {1}".format(nbLigne, res))
                sortie.write("Case #{0}: {1}\n".format(nbLigne, res))
            nbLigne += 1
    sortie.close()


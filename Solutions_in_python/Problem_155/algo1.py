

def createfile(file) :
    file = open(file, "w")
    return file
    

def lire(monfichier) :
    oujecris = createfile("answer.out")
    file = open(monfichier, "r")
    nombredelignes = int(file.readline())
    for i in range(nombredelignes) :
        maligne = file.readline()
        mesinfos = maligne.split(" ")

        # shymax est le premier de chaque ligne
        shymax = int(mesinfos[0])
        # combienjenai
        combienjenai = 0
        invitesnec = 0

        # boucle sur les spectateurs
        for j in range(0,shymax+1) :
            #
            rangactuel = j
            combienilmenfaut = int(mesinfos[1][j])

            # je dois vérifier que j'en ai assez
            # pour faire lever ceux de ce rang
            while(combienjenai < rangactuel) :
                combienjenai = combienjenai + 1
                invitesnec = invitesnec + 1

            combienjenai += combienilmenfaut
                
            
        #print("Case #",i+1,': ', invitesnec,sep='',end='\n')
        aecrire = "Case #"+str(i+1)+": "+str(invitesnec)+ "\n"
        oujecris.write(aecrire)
        
    file.close()


lire("A-large.in")
    

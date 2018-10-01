f=open("B-large.in", "r")
listeResults=[]
listeDonnees=[]
cFarm=0.0
fSupp=0.0
xEnd=0.0
produce=2.0
nbTest = int(f.readline())

for ligne in f:
    trouve=False
    time=0.0
    produce=2.0
    TempsPourObtenirUnCookie=0.0
    listeDonnees=ligne.rstrip('\n\r').split(" ")
    cFarm=float(listeDonnees[0])
    fSupp=float(listeDonnees[1])
    xEnd=float(listeDonnees[2])
    TempsPourObtenirUnCookie=xEnd/produce
    TempsPourObtenirUnCookieAvecFerme=(cFarm/produce)+(xEnd/(produce+fSupp))
    if TempsPourObtenirUnCookie<TempsPourObtenirUnCookieAvecFerme:
        listeResults.append(TempsPourObtenirUnCookie)
    else:
        while not trouve :
            time+=(cFarm/produce)
            produce+=fSupp
            TempsPourObtenirUnCookieAvecFerme=(cFarm/produce)+(xEnd/(produce+fSupp))
            TempsPourObtenirUnCookie=xEnd/produce
            if TempsPourObtenirUnCookie<TempsPourObtenirUnCookieAvecFerme:
                listeResults.append(TempsPourObtenirUnCookie+time)
                trouve=True


f.close()
f=open("Output.txt", "w")
z=0
while z < nbTest:

    f.write("Case #"+ str(z+1)+": "+str(listeResults[z])+'\n')

    z+=1
f.close()

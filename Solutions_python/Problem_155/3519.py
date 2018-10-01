casos=raw_input()
k=1
while k<casos:
    caso=str(k)
    n=raw_input()
    n=n.split()
    gente=n[1]
    i=1
    bandera=0
    suma=0
    while i<len(gente):
        j=0
        suma=0
        while j<i:
            numero=int(gente[j])
            suma=suma+numero
            j=j+1
        total=suma+bandera
        if total<i:
            bandera=bandera+1
        i=i+1
    bandera=str(bandera)
    print "Case #"+caso+": "+bandera
    k=k+1

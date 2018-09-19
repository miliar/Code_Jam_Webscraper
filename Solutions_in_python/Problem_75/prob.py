f=open("inpa.in")
fo=open("saida.out","w")
s=f.readline()
n=int(s)
for i in range(n):
    s=f.readline()[:-1]
    linea=s.split(' ')
    comb=int(linea[0])
    combinacion=[]
    resultado=[]
    for ic in range(comb):
        combinacion.append("".join(sorted(linea[1+ic][:-1])))
        resultado.append(linea[1+ic][-1])
    opuestos=[]
    nOpuest=int(linea[1+comb])

    for io in range(nOpuest):
        opuestos.append("".join(sorted(linea[2+comb+io])))
    nsec=int(linea[nOpuest+comb+2])
    secuencia=linea[nOpuest+comb+3]

    resp=""
    for c in secuencia:
        if len(resp)==0: resp+=str(c)
        else:
            tmpstr="".join(sorted(resp[0]+c))
            if tmpstr in combinacion:
                pos= combinacion.index(tmpstr)
                resp=resultado[pos]+resp[1:]            
            else:
                #procurar em opuestos
                for r in resp:
                    tmpcomb="".join(sorted(r+c))
                    if tmpcomb in opuestos:
                        resp=""
                        break
                if resp!="":
                    resp=c+resp
    resp=resp[::-1]

    #print ""    
    #print linea    
    #print opuestos
    #print combinacion
    #print resultado
    respuesta="["
    for r in resp:
        respuesta+=r+", "
    if respuesta!="[":
        respuesta=respuesta[:-2]
    respuesta+="]"
    fo.write("Case #"+str(i+1)+": "+respuesta+"\n")
    #print "Case #",str(i+1),": ",respuesta

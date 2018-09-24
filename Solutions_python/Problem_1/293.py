def GetData():
    global ifile
    n=int(ifile.readline())
    entries=[]
    ant=""

    for i in range(n):
        l=ifile.readline()
        l=l.replace('\n','')
        entries.append(l)

        ant=l

    return entries

def Choose(engines, queries):
    global odebug
    #calcula as distancia
    ecount={}
    for e in engines:
        ecount[e]=len(queries)+1

    for e in engines:
        for i, q in enumerate(queries):
            if q==e:
                ecount[e]=i
                break

    print ecount

    #procura o mais distante
    distancia=-1
    distante=""
    
    for e, d in ecount.items():
        if d>distancia:
            distancia=d
            distante=e

    print distante
    
    escolhido=distante

    return distante

    

def Best(engines, queries):
    #choose de first engine
    engine=Choose(engines, queries)
    odebug.write("START: %s\n" % engine)

    best=len(queries)
    count=0

    for q, query in enumerate(queries):
        if engine==query:
            count=count+1
            engine=Choose(engines, queries[q:])
            odebug.write("ESCOLHA: %03i - %s\n" % (q, engine))

    return count
            


ifile=file("A-large.in.txt","r")
ofile=file("saida.txt","w")
odebug=file("debug.txt","w")

casos=int(ifile.readline())


for caso in range(casos):
    engines=GetData()
    queries=GetData()

    print >> odebug,"caso %i =============================================" % (caso+1)
    print >> odebug, "******engines"
    for e in engines:
        print >> odebug, e
    print >> odebug, "######queries"
    for qn, q in enumerate(queries):
        odebug.write("%03i - %s\n" % (qn,q))

    if len(queries)==0:
        best=0
    else:
        best=Best(engines,queries)
        
    saida="Case #%i: %i\n" % (caso+1,best)
    print >> odebug, saida
    ofile.write(saida)

    
ifile.close()
ofile.close()
odebug.close()

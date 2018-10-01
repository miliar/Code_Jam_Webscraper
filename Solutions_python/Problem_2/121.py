def hora2numero(strHoras):
    datos=strHoras.split(':')
    hora=int(datos[0])
    minutos=int(datos[1])
    return hora*60+minutos;


class Viaje:
    partida=None
    llegada=None

    def __init__(self, partida, llegada):
        self.partida=partida
        self.llegada=llegada
        

class Celda:
    TRENDISPONIBLE=1
    PARTIDA=2
    TRENRESERVADO=3

    tipo=None
    tiempo=None

    def __init__(self, tipo, tiempo):
        self.tipo=tipo
        self.tiempo=tiempo



def insertar(lineaTiempo, celda):
    i=0
    N=len(lineaTiempo)

    while i<N:
        if lineaTiempo[i].tiempo == celda.tiempo :
            if celda.tipo==Celda.TRENDISPONIBLE :
                break
        elif lineaTiempo[i].tiempo > celda.tiempo :
            break
        i+=1

    lineaTiempo.insert(i,celda)

            

def crearLineasTiempo(viajesAB, viajesBA, T):
    lineaTiempoA=[]
    lineaTiempoB=[]

    for viaje in viajesAB:
        celdaPartida=Celda(Celda.PARTIDA, viaje.partida)
        celdaTrenDisp=Celda(Celda.TRENDISPONIBLE, viaje.llegada+T  ) #<<<T!

        insertar(lineaTiempoA, celdaPartida)
        insertar(lineaTiempoB, celdaTrenDisp)

    for viaje in viajesBA:
        celdaPartida=Celda(Celda.PARTIDA, viaje.partida)
        celdaTrenDisp=Celda(Celda.TRENDISPONIBLE, viaje.llegada+T ) #<<<T!

        insertar(lineaTiempoB, celdaPartida)
        insertar(lineaTiempoA, celdaTrenDisp)
        
    return lineaTiempoA, lineaTiempoB


def contarTrenesNecesarios(lineaTiempo):
    necesarios=0
    i=0
    while i<len(lineaTiempo):
        if lineaTiempo[i].tipo==Celda.PARTIDA :
            #buscar hacia atras un trendisponible
            encontrado=False
            k=i-1            
            while k>=0 :
                if lineaTiempo[k].tipo==Celda.TRENDISPONIBLE:
                    encontrado=True
                    lineaTiempo[k].tipo=Celda.TRENRESERVADO
                    k=-1 #break
                k-=1

            if not encontrado :
                necesarios+=1
        i+=1

    return necesarios



def leerCaso(fr):
    T=int(fr.readline())
    datos=fr.readline().split(' ')
    NA=int(datos[0])
    NB=int(datos[1])

    viajesAB=[]
    viajesBA=[]
    
    i=0
    while i<NA:
        datosHoras=fr.readline().split(' ')
        hora1=hora2numero(datosHoras[0])
        hora2=hora2numero(datosHoras[1])
        viajesAB.append(Viaje(hora1,hora2))
        i+=1

    i=0
    while i<NB:
        datosHoras=fr.readline().split(' ')
        hora1=hora2numero(datosHoras[0])
        hora2=hora2numero(datosHoras[1])
        viajesBA.append(Viaje(hora1,hora2))
        i+=1
    

    lineaTiempoA, lineaTiempoB = crearLineasTiempo(viajesAB, viajesBA, T)
    necesariosA=contarTrenesNecesarios(lineaTiempoA)
    necesariosB=contarTrenesNecesarios(lineaTiempoB)

    return necesariosA, necesariosB



fr=open('B-large.in','r')
fw=open('B-large.out','w')

numCasos=int(fr.readline())

i=1
while i<=numCasos:
    necA, necB=leerCaso(fr)
    fw.write("Case #%d: %d %d\n" % (i, necA, necB))

    i+=1

fr.close()
fw.close()


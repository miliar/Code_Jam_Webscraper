from decimal import *


def play_wood_bad(naomi, kem, count_box, trampa):
    trampa = 0
    for madera in naomi:
        madera_kem = kem[0]
        if madera_kem < madera:
            trampa +=1
        else:
            madera_kem = kem[len(kem)-1]
        ubicacion = kem.index(madera_kem) 
        kem.pop(ubicacion)
    return trampa



def kem_choose_good(naomi_box_choose, kem):
    madera=0
    for madera in kem:
        if madera > naomi_box_choose:
            return madera
    return kem[0]
def play_wood_good(naomi, kem, count_box, trampa):
    trampa = 0
    for madera in naomi:
     
        madera_kem = kem_choose_good(madera, kem)
        if madera_kem < madera:
            trampa +=1
        ubicacion = kem.index(madera_kem) 
        kem.pop(ubicacion)
    return trampa

if __name__ == "__main__":
    getcontext().prec = 28

    file_name = "entrada4"
    objecto_archivo = open(file_name, 'r')
    count_case = int(objecto_archivo.readline()[:-1])

    for number_case in range(0, count_case): 
        trampa = 0
        optimo = 0
        frase = "Case #"+str(number_case +1)+": "
        cant_cajas = int(objecto_archivo.readline()[:-1])
        naomi_box_ = objecto_archivo.readline()[:-1]
        naomi_box = naomi_box_.split(" ")
        naomi_box = [Decimal(x) for x in naomi_box]
        kem_box_ = objecto_archivo.readline()[:-1]
        kem_box =  kem_box_.split(" ")
        kem_box = [Decimal(x) for x in kem_box ]
        naomi_box.sort()
        kem_box.sort()


        naomi_box2 = naomi_box_.split(" ")
        naomi_box2 = [Decimal(x) for x in naomi_box2]
        kem_box2 =  kem_box_.split(" ")
        kem_box2 = [Decimal(x) for x in kem_box2 ]
        naomi_box2.sort()
        kem_box2.sort()
        bad = play_wood_bad(naomi_box, kem_box, cant_cajas, trampa)
        good = play_wood_good(naomi_box2, kem_box2, cant_cajas, optimo)
        print frase + str(bad) + " "+ str(good)

    objecto_archivo.close()

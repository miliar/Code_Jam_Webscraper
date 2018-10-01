
entrada = open("A-large.in", "r")
salida = open("output.txt", "w")
casos = int(entrada.readline())

def ganador(caso, suma, salida):
    if suma == 36 or suma == 32:
        salida.write("Case #"+str(caso+1)+": O won\n")
        return True
    if suma == 4 or suma == 8:
        salida.write("Case #"+str(caso+1)+": X won\n")
        return True
    return False

for caso in range(casos):
    tabla = []

    tabla.append(map(int,entrada.readline().strip().replace("X","1").replace("O","9").replace("T","5").replace(".","0")))
    tabla.append(map(int,entrada.readline().strip().replace("X","1").replace("O","9").replace("T","5").replace(".","0")))
    tabla.append(map(int,entrada.readline().strip().replace("X","1").replace("O","9").replace("T","5").replace(".","0")))
    tabla.append(map(int,entrada.readline().strip().replace("X","1").replace("O","9").replace("T","5").replace(".","0")))
    _ = entrada.readline()

    if ganador(caso, tabla[0][0]+tabla[0][1]+tabla[0][2]+tabla[0][3], salida):
        continue
    if ganador(caso, tabla[1][0]+tabla[1][1]+tabla[1][2]+tabla[1][3], salida):
        continue
    if ganador(caso, tabla[2][0]+tabla[2][1]+tabla[2][2]+tabla[2][3], salida):
        continue
    if ganador(caso, tabla[3][0]+tabla[3][1]+tabla[3][2]+tabla[3][3], salida):
        continue         
    if ganador(caso, tabla[0][0]+tabla[1][0]+tabla[2][0]+tabla[3][0], salida):
        continue
    if ganador(caso, tabla[0][1]+tabla[1][1]+tabla[2][1]+tabla[3][1], salida):
        continue
    if ganador(caso, tabla[0][2]+tabla[1][2]+tabla[2][2]+tabla[3][2], salida):
        continue
    if ganador(caso, tabla[0][3]+tabla[1][3]+tabla[2][3]+tabla[3][3], salida):
        continue
    if ganador(caso, tabla[0][0]+tabla[1][1]+tabla[2][2]+tabla[3][3], salida):
        continue
    if ganador(caso, tabla[3][0]+tabla[2][1]+tabla[1][2]+tabla[0][3], salida):
        continue
    
    if tabla[0].count(0) + tabla[1].count(0) + tabla[2].count(0) + tabla[3].count(0) == 0:
        salida.write("Case #"+str(caso+1)+": Draw\n")       
    else:
        salida.write("Case #"+str(caso+1)+": Game has not completed\n")

entrada.close()
salida.close()

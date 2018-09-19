arq = open('A-small-attempt0.in', 'r')
cases = int(arq.readline())

for quantidade in range(cases):
    resposta1 = arq.readline()
    cartas1 = []
    cartas2 = []
    pontos = 0
    resultado = ""
    
    for linha in range(4):
            lerLinha = arq.readline()
            cartas1.append(lerLinha.split())
    
    resposta2 = arq.readline()
    
    
    for linha in range(4):
            lerLinha = arq.readline()
            cartas2.append(lerLinha.split())
    
    i=int(resposta1) - 1
    
    i2=int(resposta2) - 1
    
    for j in range(4):
        for j2 in range(4):
            if (cartas1[i][j] == cartas2[i2][j2]):
                pontos = pontos+1
                resultado = cartas1[i][j]
    #Case #1: 7
    #Case #2: Bad magician!
    #Case #3: Volunteer cheated! 
    if pontos == 0:
        resultado = "Volunteer cheated!"
    elif pontos > 1:
        resultado = "Bad magician!"
    
    completa = "Case #" + str((quantidade+1)) + ": " + resultado + '\n'
    arq_out = open('sample.out', 'a+')
    arq_out.write(completa)
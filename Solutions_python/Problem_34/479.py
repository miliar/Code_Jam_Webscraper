entrada = open('A-large.in')
saida = open('A-large.out', 'w')

dados = entrada.readline()
tamanho, palavras, testes = dados.split(' ')
tamanho, palavras, testes = int(tamanho), int(palavras), int(testes)

dicionario = []
for i in range(palavras):
    palavra = entrada.readline().strip()
    dicionario.append(palavra)

casos = []
for i in range(testes):
    caso = entrada.readline().strip()
    casos.append(caso)

entrada.close()

def processar_caso(caso):
    possibilidades = []
    letras = ''
    aberto = False
    for letra in caso:
        if letra == '(':
            aberto = True
            continue
        elif letra == ')':
            aberto = False
            possibilidades.append(letras)
            letras = ''
            continue
        else:
            if aberto:
                letras += letra
            else:
                possibilidades.append(letra)

    r = 0
    for palavra in dicionario:
        for i in range(tamanho):
            if not palavra[i] in possibilidades[i]:
                break
            elif i == tamanho - 1:
                r += 1
    
    return r

i = 1
for caso in casos:
    resultado = processar_caso(caso)
    saida.write('Case #%d: %d\n' % (i, resultado))
    i += 1

saida.close()

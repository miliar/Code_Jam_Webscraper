import psyco
psyco.full()

entrada = open('B-small.in')
saida = open('B-small.out', 'w')

quantidade_casos = int(entrada.readline().strip())

casos = []
for i in range(quantidade_casos):
    casos.append(entrada.readline().strip())

entrada.close()

def resolver_caso(numero):
    original = [numero.count('0'), numero.count('1'), numero.count('2'), numero.count('3'), numero.count('4'), numero.count('5'), numero.count('6'), numero.count('7'), numero.count('8'), numero.count('9')]
    a = int(numero)
    while 1:
        a += 1
        b = str(a)
        c = [b.count('0'), b.count('1'), b.count('2'), b.count('3'), b.count('4'), b.count('5'), b.count('6'), b.count('7'), b.count('8'), b.count('9')]
        valido = True
        for i in range(10):
            if original[i] != c[i]:
                if i > 0:
                    valido = False
                    break
                #if original[i] > 0:
                #    if c[i] - original[i] != 1:
                #        valido = False
                #        break
        if valido:
            break
    return b

numero_caso = 1
for caso in casos:
    print numero_caso, caso
    resultado = resolver_caso(caso)
    saida.write('Case #%d: %s\n' % (numero_caso, resultado))
    numero_caso += 1

saida.close()

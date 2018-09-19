entrada = open('B-large.in')
saida = open('B-large.out', 'w')

testes = int(entrada.readline().strip())
casos = []
for i in range(testes):
    h, w = entrada.readline().strip().split(' ')
    h, w = int(h), int(w)
    caso = []
    for j in range(h):
        tmp = entrada.readline().strip().split(' ')
        caso.append([int(altura) for altura in tmp])
    casos.append(caso)

entrada.close()

def encontrar_banheira(caso, x, y):
    n = (x, y - 1)
    w = (x - 1, y)
    e = (x + 1, y)
    s = (x, y + 1)
    
    a_altura = caso[y][x]
    n_altura = w_altura = e_altura = s_altura = -1
    
    n_pode = w_pode = e_pode = s_pode = False
    
    if y > 0:
        n_altura = caso[n[1]][n[0]]
        n_pode = n_altura < a_altura
    if x > 0:
        w_altura = caso[w[1]][w[0]]
        w_pode = w_altura < a_altura
    if x < len(caso[y]) - 1:
        e_altura = caso[e[1]][e[0]]
        e_pode = e_altura < a_altura
    if y < len(caso) - 1:
        s_altura = caso[s[1]][s[0]]
        s_pode = s_altura < a_altura

    if n_pode == False and w_pode == False and e_pode == False and s_pode == False:
        return (x, y)
    else:
        menor = None
        menor_altura = None
        if n_pode:
            if menor == None:
                menor = n
                menor_altura = n_altura
            elif n_altura < menor_altura:
                menor = n
                menor_altura = n_altura
        if w_pode:
            if menor == None:
                menor = w
                menor_altura = w_altura
            elif w_altura < menor_altura:
                menor = w
                menor_altura = w_altura
        if e_pode:
            if menor == None:
                menor = e
                menor_altura = e_altura
            elif e_altura < menor_altura:
                menor = e
                menor_altura = e_altura
        if s_pode:
            if menor == None:
                menor = s
                menor_altura = s_altura
            elif s_altura < menor_altura:
                menor = s
                menor_altura = s_altura
        
        return encontrar_banheira(caso, menor[0], menor[1])
        #if n_pode and n_altura <= w_altura and n_altura <= e_altura and n_altura <= s_altura:
        #    return encontrar_banheira(caso, n[0], n[1])
        #elif w_pode and w_altura <= e_altura and w_altura <= s_altura:
        #    return encontrar_banheira(caso, w[0], w[1])
        #elif e_pode and e_altura <= s_altura:
        #    return encontrar_banheira(caso, e[0], e[1])
        #else:
        #    return encontrar_banheira(caso, s[0], s[1])

def resolver_caso(caso):
    r = ''
    identificacao = 'a'
    banheiras = {}
    for y in range(len(caso)):
        for x in range(len(caso[y])):
            tmp = encontrar_banheira(caso, x, y)
            if not banheiras.has_key(tmp):
                banheiras[tmp] = identificacao
                identificacao = chr(ord(identificacao) + 1)
            r += banheiras[tmp] + ' '
        r = r.strip() + '\n'
    return r

i = 1
for caso in casos:
    resultado = resolver_caso(caso)
    saida.write('Case #%d:\n%s' % (i, resultado))
    i += 1

saida.close()


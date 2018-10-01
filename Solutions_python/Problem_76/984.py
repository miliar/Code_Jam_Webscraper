import itertools

def to_bin(x, count=20):
    return "".join(map(lambda y:str((x>>y)&1), range(count-1, -1, -1)))
        
def soma_binaria_patrick(a, b):
    total = ''
    for i in reversed(range(0, 20)):
        if a[i] == b[i]:
            total = '0' + total
        else:
            total = '1' + total
    return total
    
def soma_patrick(lista):
    total = '00000000000000000000'
    for v in lista:
        total = soma_binaria_patrick(total, to_bin(v))
    return int(total, 2)
        

def soma_sean(lista):
    return sum(lista)
    
def is_possivel(valores):
    melhor_soma_sean = 0
    contagem = len(valores)
    for i in range(1, contagem):
        for it in itertools.combinations(valores, i):
            lista_sean = list(it)
            lista_patrick = []
            lista_patrick.extend(valores)
            for x in lista_sean:
                lista_patrick.remove(x)

            total_sean = soma_sean(lista_sean)
            if soma_patrick(lista_sean) == soma_patrick(lista_patrick):
                if total_sean > melhor_soma_sean:
                    melhor_soma_sean = total_sean

    if melhor_soma_sean > 0:
        return str(melhor_soma_sean)
    else:
        return 'NO'
            
            

with open('C-small-attempt1.in', 'r') as f:
    casos = int(f.readline())
    for i in range(1, casos+1):
        n_doces = f.readline()
        valores = [int(s.strip()) for s in f.readline().split(' ') if s]
        possivel = is_possivel(valores)
        print 'Case #%d: %s' % (i, possivel)
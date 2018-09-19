def sorting_key(elem):
    return elem[1]

N = int(raw_input())
case_number = 1

for i in xrange(N):
    P, K, L = map(int, raw_input().split())

    entradas = map(int, raw_input().split())
    
    frequencias = enumerate(entradas)
    
    frequencias = sorted(frequencias, key=sorting_key, reverse=True)
    
    custos = {}
    for i in xrange(len(frequencias)):
        custos[frequencias[i][0]] = i/K +1
    
    
    custo = 0
    for frequencia in frequencias:
        custo += custos[frequencia[0]]*frequencia[1]
        
    print "Case #%d: %d" % (case_number, custo)
    case_number += 1
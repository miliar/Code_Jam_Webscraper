entrada = open("B-large.in", "r")
saida = open("b_out.txt", "w")


n = int(entrada.readline())

for i in range(1,n+1):
    limite = list(reversed(list(map(int, list(entrada.readline().strip())))))
    maior = []

    #print(limite)

    # se tudo esta ordenado
    if limite == list(reversed(sorted(limite))):
        t = "".join(map(str,reversed(limite)))
        print("Case #%i: %i" % (i,int(t)))
        saida.write("Case #%i: %i\n" % (i,int(t)))
        continue

    # senao
    ok = False
    
    for k in range(len(limite)-1):

        if limite[k:] == list(reversed(sorted(limite[k:]))):
            print(limite[k:])
            t = "".join(map(str,reversed(limite[k:])))+"".join(map(str,reversed(maior)))
            print("Case #%i: %i" % (i,int(t)))
            saida.write("Case #%i: %i\n" % (i,int(t)))
            ok = True
            break

        if ok:
            break
        
        maior.append(9)
        limite[k+1] -= 1
        
        #if limite[k] < limite[k+1] or limite[k] == 0:
        #    maior.append(9)
        #    limite[k+1] -= 1
            
        #elif limite[k] == limite[k+1] and limite[k] != 9:
        #    maior.append(9)
        #    limite[k+1] -= 1
        #else:
        #    maior.append(limite[k])

            
        #print(limite)
        #print(maior)

    if not ok:
        maior.append(limite[-1])
        #print(maior)
    
        t = "".join(map(str,reversed(maior)))
        print("Case #%i: %i" % (i,int(t)))
        saida.write("Case #%i: %i\n" % (i,int(t)))

entrada.close()
saida.close()

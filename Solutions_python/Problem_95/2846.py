mapa = {}

linha = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv z q'
respo = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up q z'

list_linha = list(linha)
list_respo = list(respo)

for i in range(len(list_linha)):
    mapa[list_linha[i]] = list_respo[i]

arquivo = open('small.txt', 'r')
quantidade = arquivo.readline()
y = 0
for entrada in arquivo:
    y = y+1
    resp = []
    for letra in list(entrada)[:-1]:
        resp.append(mapa[letra])
    saida = ''.join(str(n) for n in resp)
    print "Case #%s: %s" % (y,saida)


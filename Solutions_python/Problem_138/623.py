import sys

def hitung(d1, d2):
    hasil = ''
    d3 = []
    nama = {}
    nao = []
    ken = []
    for x in d1.split():
        d3.append(x)
        nama[x] = 'nao'
        nao.append(x)
    for x in d2.split():
        d3.append(x)
        nama[x] = 'ken'
        ken.append(x)
    # untuk deception war
    d3.sort(reverse=True)
    naob = 0
    h1 = 0
    for key in d3:
        if nama[key] == 'nao':
            naob += 1
        if nama[key] == 'ken':
            if naob > 0:
                h1 += 1
                naob -= 1
    # untuk war
    nao.sort(reverse=True)
    ken.sort()
    h2 = 0
    for xn in nao:
        adalb = False
        for xk in ken:
            if float(xk) > float(xn):
                ken.remove(xk)
                adalb = True
                break
        if adalb == False:
            ken.pop(0)
            h2 += 1
    hasil = str(h1) + ' ' + str(h2)
    return hasil

i = 0
nomor = 1
for baris in sys.stdin:
    data = baris.strip()
    if i == 0:
        n = int(data)
    elif i == 1:
        m = int(data)
    elif i == 2:
        d1 = data
    elif i == 3:
        d2 = data
    if i == 3:
        jawab = hitung(d1, d2)
        print 'Case #' + str(nomor) + ': ' + jawab
        i = 0
        nomor += 1
    i += 1

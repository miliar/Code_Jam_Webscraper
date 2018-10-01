import sys

def hitung(data):
    hasil = 0
    a = data.split()
    C = float(a[0])
    F = float(a[1])
    X = float(a[2])
    spf = 2
    tku = 0
    t = X / spf
    while True:
        tku = tku + (C / spf)
        spf = spf + F
        talt = tku + (X / spf)
        if talt > t:
            hasil = t
            break
        t = talt
    return str(hasil)

i = 0
nomor = 1
for baris in sys.stdin:
    data = baris.strip()
    if i == 0:
        n = int(data)
    else:
        jawab = hitung(data)
        print 'Case #' + str(nomor) + ': ' + jawab
        nomor += 1
    i += 1

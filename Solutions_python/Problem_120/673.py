#! /usr/bin/python

import sys

def hitung(teks):
    sel = teks.split(' ')
    r = int(sel[0])
    t = int(sel[1])
    ring = 0
    while True:
        luas = (2 * r) + 1
        if t >= luas:
            ring += 1
            r += 2
            t -= luas
        else:
            return ring


i = 0
nomor = 1
data = sys.stdin.readlines()
for baris in data:
    if i == 0:
        jumlahsoal = int(baris)
    else:
        baris = baris.strip()
        hasil = hitung(baris)
        jawab = "Case #" + str(nomor) + ": " + str(hasil)
        print jawab
        nomor += 1
    i += 1
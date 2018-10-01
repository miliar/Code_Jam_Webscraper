import string
import math

input = 'A-large.in'
output = 'output-a-large'
try:
    f = open(input, 'r')
except:
    exit('file: ' + input + ' non trovato')
try:
    out = open(output, 'w')
except:
    exit('file: ' + output + ' non trovato')

T = int(f.readline())

for index in range(T):
    N = int(f.readline())
    a = []
    wp = []
    owp = []
    oowp = []
    
    for i in range(N):
        a.append(f.readline())

    for i in range(N):
        wptot = 0
        wpcount = 0
        for j in range(N):
            if a[i][j] != '.':
                wpcount += 1
                if a[i][j] == '1':
                    wptot += 1
        wp.append(float(wptot)/float(wpcount))
        
    for i in range(N):
        owptot = float(0)
        owpcount = 0
        for k in range(N):
            if k != i and a[i][k] != '.':
                wptot = 0
                wpcount = 0
                owpcount += 1
                for j in range(N):
                    if i != j and a[k][j] != '.':
                        wpcount += 1
                        if a[k][j] == '1':
                            wptot += 1
                owptot += float(wptot)/float(wpcount)
        owp.append(float(owptot)/float(owpcount))
    
    for i in range(N):
        oowptot = float(0)
        oowpcount = 0
        for j in range(N):
            if i != j and a[i][j] != '.':
                oowptot += owp[j]
                oowpcount += 1
        oowp.append(float(oowptot)/float(oowpcount))
    
    out.write('Case #' + str(index + 1) + ':\n')
    for i in range(N):
        rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]
        out.write(str(rpi) + '\n')
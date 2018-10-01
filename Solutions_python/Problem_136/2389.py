
def calculo(c,f,x,tacum,inc):
    print c
    print f
    print x
    print "calculo"
    tout=x/float(inc)
    print tout
    tcalculado=x/inc
    tanterior=100000000000000000
    tfarm=0
    while tcalculado<tanterior:
        tanterior=tcalculado
        tfarm+=(c/inc)
        inc=inc+f
        tCooki=x/inc
        tcalculado=tfarm+tCooki
    
    print "solucion"  
    print tanterior  
    return str(tanterior)   

f= open('B-large.in.txt')
imput= f.read().splitlines()

fOut = open('CookieClickerlarge.out', 'w')

ncases=int(imput[0])
#del imput[0]

#prueba:

for a in range(1,ncases+1):
    c,f,x=imput[int(a)].split()
    c=float(c)
    f=float(f)
    x=float(x)
    solucion=calculo(c,f,x,0,2)
    fOut.write("Case #"+str(a)+": "+solucion+"\n")  

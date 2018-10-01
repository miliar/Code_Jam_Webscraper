import sys
sys.stdin=open("A-small-attempt1.in","r")
sys.stdout=open("output.txt","w")

def magia(w):
        
    lista1=raw_input().split( ' ' )
    lista2=raw_input().split( ' ' )
    lista3=raw_input().split( ' ' )
    lista4=raw_input().split( ' ' )

    if w==1:
        e=lista1
        return e
    if w==2:
        e=lista2
        return e
    if w==3:
        e=lista3
        return e
    if w==4:
        e=lista4
        return e
    
x=int(raw_input())
for i in range(0,x):
    w=int(raw_input())
    q=magia(w)
    w=int(raw_input())
    e=magia(w)
    
    contador=0
    numero=1
    
    for m in range(0,4):
        for n in range(0,4):
            if q[n]==e[m]:
                numero=q[n]
                contador=contador+1
    if contador>1:
        print 'Case #'+str(i+1)+': Bad magician!'
    if contador==0:
        print 'Case #'+str(i+1)+': Volunteer cheated!'
    if contador==1:
        print 'Case #'+str(i+1)+':',numero
    
    
    

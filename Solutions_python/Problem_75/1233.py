import string

def sAlist(string):
    res=[]
    for x in string:
        if (x!=' ' and x!='\n'):
            res.append(x)
    return res

def combinan(char1, char2, lista):
    flag=False
    res="false"
    for x in lista:
        if ((char1==x[0] and char2==x[1]) or (char2==x[0] and char1==x[1])):
            flag=True
            res=x[2]
    return (flag, res)

def opposed(char1, char2, lista):
    res=False
    for x in lista:
        if ((char1==x[0] and char2==x[1]) or (char2==x[0] and char1==x[1])):
            res=True
    return res

def borrara(char1,invokes,lista):
    res=False
    for x in invokes:
        if opposed(char1,x,lista):
            res=True
            break
    return res

def resolver(combinaciones,oposiciones,string):
    invokes=sAlist(string)
    res=[]
    for x in invokes:
        if len(res)==0:
            res.append(x)
        else:
            combinaran=combinan(res[-1],x,combinaciones)
            if combinaran[0]:
                res.pop()
                res.append(combinaran[1])
            else:
                limpia=borrara(x,res,oposiciones)
                if limpia:
                    res=[]
                else:
                    res.append(x)
    return res


f=open('B-small-attempt4.txt','r')
out=open('res.txt','w')

def armarInst(caso,lista):
    combs=[]
    ops=[]
    invokes=''
    if (len(lista)==0 or len(lista)==1):
        return
    else:
        cantCombs=int(lista.pop(0))
        for x in range(0,cantCombs,3):
            combs.append((lista.pop(0),lista.pop(0),lista.pop(0)))
        cantOps=int(lista.pop(0))
        for x in range(0,cantOps,2):
            ops.append((lista.pop(0),lista.pop(0)))
        cantLetras=int(lista.pop(0))
        if(lista[0]==0):
            cantLetras=10
            lista.pop(0)
        for x in lista:
            invokes+=x
    res=resolver(combs,ops,invokes)
    texto="Case #"
    texto+=str(i)
    texto+=": ["
    for x in res:
        texto+=x
        texto+=', '
    texto=texto.rstrip()
    texto=texto.rstrip(',')
    texto+=']\n'
    out.write(texto)
i=1
for line in f:
    linea=sAlist(line)
    armarInst(i,linea)
    i+=1




out.close()
f.close()
    

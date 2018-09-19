op = {'11':'1','1i':'i','1j':'j','1k':'k','i1':'i','ii':'-1','ij':'k','ik':'-j','j1':'j','ji':'-k','jj':'-1','jk':'i','k1':'k','ki':'j','kj':'-i','kk':'-1',
      '-11':'-1','-1i':'-i','-1j':'-j','-1k':'-k','-i1':'-i','-ii':'1','-ij':'-k','-ik':'j','-j1':'-j','-ji':'k','-jj':'1','-jk':'-i','-k1':'-k','-ki':'-j','-kj':'i','-kk':'1',
      '1-1':'-1','1-i':'-i','1-j':'-j','1-k':'-k','i-1':'-i','i-i':'1','i-j':'-k','i-k':'j','j-1':'-j','j-i':'k','j-j':'1','j-k':'-i','k-1':'-k','k-i':'-j','k-j':'i','k-k':'1'}

def buscar_i(palabra):
    if palabra[0] == 'i':
        return True,palabra[1:]
    else:
        l1 = palabra[0]
        for y in range(1,len(palabra)):
            l1 = op[l1+palabra[y]]
            if l1 == 'i':
                return True, palabra[y+1:]
        return False, ''

def buscar_j(palabra):
    if palabra[0] == 'j':
        return True, palabra[1:]
    else:
        l1 = palabra[0]
        for y in range(1,len(palabra)):
            l1 = op[l1+palabra[y]]
            if l1 == 'j':
                return True, palabra[y+1:]
        return False, ''

def buscar_k(palabra):
    if len(palabra) == 1 and palabra == 'k':
        return True
    else:
        l1 = palabra[0]
        for y in range(1, len(palabra)):
            l1 = op[l1+palabra[y]]
        if l1 == 'k':
            return True
        else:
            return False
        

f = open("C-small-attempt0.in", "r")
s = open("output.txt","w")
t = int (f.readline())
for i in range(0,t):
    ent = f.readline().split(' ')
    l = int(ent[0])
    x = int(ent[1])
    palabra = f.readline()
    palabra = palabra[:-1]
    palabra = palabra*x
    if l*x < 3:
        s.write("Case #%d: NO\n" % (i+1))
    elif l*x == 3 and palabra != 'ijk':
        s.write("Case #%d: NO\n" % (i+1))
    elif l==1:
        s.write("Case #%d: NO\n" % (i+1))
    else:
        consiguio_i, palabra = buscar_i(palabra)
        if consiguio_i == False:
            s.write("Case #%d: NO\n" % (i+1))
        elif len(palabra)<2:
            s.write("Case #%d: NO\n" % (i+1))
        elif palabra == 'jk':
            s.write("Case #%d: YES\n" % (i+1))
        else:
            consiguio_j, palabra = buscar_j(palabra)
            if consiguio_j == False:
                s.write("Case #%d: NO\n" % (i+1))
            elif palabra == 'k':
                s.write("Case #%d: YES\n" % (i+1))
            else:
                consiguio_k = buscar_k(palabra)
                if consiguio_k == True:
                    s.write("Case #%d: YES\n" % (i+1))
                else:
                    s.write("Case #%d: NO\n" % (i+1))

f.close()
s.close()

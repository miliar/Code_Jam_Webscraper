#!/usr/bin/python
########################
# hucruz92@gmail.com   #
########################

tabla = {"1i":"i","1j":"j","1k":"k",
         "-1i":"-i","-1j":"-j","-1k":"-k",
         "ii":"-1","ij":"k","ik":"-j",
         "-ii":"1","-ij":"-k","-ik":"j",
         "ji":"-k","jj":"-1","jk":"i",
         "-ji":"k","-jj":"1","-jk":"-i",
         "ki":"j","kj":"-i","kk":"-1",
         "-ki":"-j","-kj":"i","-kk":"1"}
def valido(linea):
    if prod(linea) == "-1":
        return True
    else:
        return False
def prod(linea):
    p = linea[0]
    for k in range(1,len(linea)):
        p = tabla[p+linea[k]]
    return p

def solve(cad):
    sol = "NO"
    if not valido(cad):
        return "NO"
    for l in range(1,len(cad)-1):
        if prod(cad[:l]) != "i":
            continue
        for c in range(l+1,len(cad)):
            if prod(cad[l:c]) != "j":
                continue
            elif prod(cad[c:]) == "k":
                return "YES"
    return "NO"

def graba(case, sol):
    global fo
    fo.write("Case #" + str(case) + ": " + str(sol) + "\n")

fi = open("C-small-attempt3.in",'r')
fo = open("C-small-attempt3.out",'w')
T = int(fi.readline())

for case in range(1,T+1):
    linea = fi.readline().split()
    print linea
    L, X = [int(n) for n in linea]
    cad = fi.readline()[:-1]
    if L == 1:
        sol= "NO"
    else :
        sol = solve(cad*X)
    graba(case, sol)

fo.close()
fi.close()

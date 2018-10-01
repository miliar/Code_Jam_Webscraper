class Candy:
    def __init__(self, n):
        if(isinstance(n , Candy)):
            self.n = n.n
        else:
            self.n = n
        self.binstr = bin(self.n)[2:]
        abits = []
        for i in self.binstr:
            abits.append(int(i))
        self.bits = abits[::-1]
        

    def __add__(self, m):
        if(isinstance(m, Candy)):
            return Candy(self.n ^ m.n)
        else:
            return Candy(self.n ^ m)

    def __radd__(self, m):
        if(isinstance(m, Candy)):
            return Candy(self.n ^ m.n)
        else:
            return Candy(self.n ^ m)

    def __int__(self):
        return n
    
    def __len__(self):
        return len(self.bits)

    def __repr__(self):
        return self.binstr + "=" + str(self.n) + ""

    def __getitem__(self, index):
        if(index >= len(self.bits) or index <0):
            print "Error: [i]"
            return -1
        else:
            return self.bits[index]
    def __cmp__(self, m):
        if(isinstance(m , Candy)):
            return self.n.__cmp__(m.n)
        else:
            return self.n.__cmp__(m)
        
    
def insertPile(aelement, Patrick, Sean, SeanReal):
    element = Candy(aelement)
    if(Patrick == 0):
        Patrick = Patrick + element
    elif(element + Sean == Patrick):
        Sean = Sean + element
        SeanReal = SeanReal + element.n
    elif(len(Patrick)<len(Sean)):
        Sean = Sean + element
        SeanReal = SeanReal + element.n
    elif(Patrick<Sean):
        Patrick = Patrick + element
    else:
        Sean = Sean + element
        SeanReal = SeanReal + element.n
    return Patrick, Sean, SeanReal
        

def candyToPile(l):
    Sean = Candy(0)
    SeanReal = 0
    lista = l[0:]
    for i in lista:
        Sean = Sean + i
        SeanReal = SeanReal + i
    if(Sean==0):
        lista.sort()
        return str(SeanReal - lista[0])
    return "NO"
        
def solver(name):
    inputstr = file(name, "r")
    output = file(name + ".out", "w")
    outstr = ""
    T = int(inputstr.readline())
    lines = inputstr.readlines()
    for i in range(T):
        N = int(lines[i*2])
        line = lines[i*2 + 1]
        ei = line.split()[0:N]
        Ci = []
        for jk in ei:
            Ci.append(int(jk))

        outstr = outstr + "Case #" + str(i+1) + ": " + candyToPile(Ci) + "\n"

            
    output.write(outstr)
    output.close()
    inputstr.close()

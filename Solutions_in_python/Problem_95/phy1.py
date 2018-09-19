lista = {}
def writetodict(a,b):
        lista[a] = b

f = open("google","r")
p = open("result","r")
m = open("mapping", "w")
x = int(f.readline())
for str in f:
        for ch in str:
                if ch == " ":
                        p.read(1)
                elif ch == "\n":
                        p.read(1)
                else:
                        writetodict(ch,p.read(1))
                        #print(ch+";"+p.read(1))

for a,b in lista.iteritems():
        m.write(a+";"+b+"\n")
m.write("z;q\n")
m.write("q;z\n")

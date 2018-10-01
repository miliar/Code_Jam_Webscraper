#Tested locally with Python 2.6.2 on OS X 10.6.0

def search(str,at,part):
    boo = "welcome to code jam"
    
    if at == len(boo):
        return 1
    
    ret = 0
    meep = str.find(boo[at],part)
    while meep != -1:
        ret += search(str,at+1,meep) % 10000
        meep = str.find(boo[at],meep+1)

    return ret

input = open('C-small.in','r')
output = open('C-small.out','w')
N = int(input.next())

for i in range(0,N):
    line = input.next()

    numPossible = search(line, 0, 0) % 10000

    output.write("Case #"+str(i+1)+": "+(str(numPossible).zfill(4))+"\n")

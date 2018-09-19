# Input: T = število vrstic, G = tekst, output: X = število piozkusa, S = prevedeno besedilo
f = open("A-small-attempt0.in","r+")

st = int(f.readline())
vrste = []
for line in f:
    vrste.append(list(line.replace('\n', '')))
    
print(st)
abecA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecG = ['y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q']
l = 0
for x in vrste:
    k = 0
    for y in x:
        if abecG.count(y)>=1:
            z = abecG.index(y)
            vrste[l][k] = abecA[z]
        k = k + 1
    l = l + 1
f.seek(0)
for x in range(st):
    f.write('Case #' + str(x + 1) + ': ' + ''.join(vrste[x]) + '\n')
    
f.close()
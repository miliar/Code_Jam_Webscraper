f = open('A-small-attempt1.in','r')
n = int(f.readline())
cases = []
for i in range(n):
    s = 'Case #'+`i+1`+': '
    c = []
    row = [0,0]
    deck = [[],[]]
    for j in range(2) :
        row[j] = int(f.readline())
        for k in range(4) :
            deck[j].append(f.readline().split())
    for x in deck[0][row[0]-1] :
        for y in deck[1][row[1]-1] :
            if x == y : c.append(x)
    if len(c)==0 : s += 'Volunteer cheated!'
    elif len(c)==1 : s += c[0]
    else : s += 'Bad magician!'
    cases.append(s)
f.close()
g = open('outputA.txt','w')
for z in cases :
    g.write(z+'\n')
g.close()
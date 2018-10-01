infile = open('in.txt','r')
lines = infile.readlines()
infile.close()
infile = open('out.txt','w')
for i in range(len(lines)):
    lines[i] = lines[i][:-1]

k = 1    
for i in range(int(lines[0])):
    data = []
    for j in range(int(lines[k])):
        k = k + 1
        l = 0
        let = []
        for z in range(len(lines[k])):
            if len(let) != 0 and let[l][0] != lines[k][z]:
                l = l + 1
                let = let + [[lines[k][z],1]]
            elif len(let) == 0:
                let = let + [[lines[k][z],1]]
            else:
                let[l][1] = let[l][1] + 1
        data = data + [let]
    k = k + 1
    a = 0
    for j in range(len(data)):
        a = a + len(data[j])
    a = a / len(data)
    ar = True
    for j in range(len(data)):
        if len(data[j]) != a:
            ar = False
            break
    if ar:
        m = 0
        for j in range(len(data[0])):
            a = 0
            for z in range(len(data)):
                if data[z][j][0] != data[0][j][0]:
                    ar = False
                    break
                else:
                    a = a + data[z][j][1]
            a = a / len(data)
            for z in range(len(data)):
                if a > data[z][j][1]:
                    m = m + (a-data[z][j][1])
                else:
                    m = m + (data[z][j][1]-a)
        if ar:
            infile.write('Case #'+str(i+1)+': '+str(m)+'\n')
        else:
            infile.write('Case #'+str(i+1)+': Fegla Won'+'\n')
    else:
        infile.write('Case #'+str(i+1)+': Fegla Won'+'\n')
infile.close()

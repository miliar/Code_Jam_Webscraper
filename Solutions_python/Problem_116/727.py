'''
Created on Apr 12, 2013

@author: Phil
'''
def isWin(row):
    xs = sum(1 if c=='X' else 0 for c in row)
    os = sum(1 if c=='O' else 0 for c in row)
    if 'T' in row:
        xs = xs+1
        os = os+1
    if xs>=4:
        return 1
    elif os>=4:
        return 2
    else:
        return 0

def winner(xoro, output, n):
    output += "Case #"+str(n)+": "+('X' if xoro==1 else 'O')+" won\n"
    return output

fname = input('In file: ')
namefile = fname.split('.')[0]

fr = open(fname, 'r')
fc = fr.read()
fr.close()

lines = fc.split('\n')
output = ""
numCases = int(lines[0])

for n in range(numCases):
    r1 = lines[5*n+1]
    r2 = lines[5*n+2]
    r3 = lines[5*n+3]
    r4 = lines[5*n+4]
    r5 = r1[0]+r2[1]+r3[2]+r4[3]
    r6 = r1[3]+r2[2]+r3[1]+r4[0]
    r7 = r1[0]+r2[0]+r3[0]+r4[0]
    r8 = r1[1]+r2[1]+r3[1]+r4[1]
    r9 = r1[2]+r2[2]+r3[2]+r4[2]
    r10 = r1[3]+r2[3]+r3[3]+r4[3]
    for r in [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]:
        result = isWin(r)
        if result:
            output = winner(result,output,n+1)
            break
    else:
        if any('.' in r for r in [r1,r2,r3,r4]):
            output += "Case #"+str(n+1)+": Game has not completed\n"
        else:
            output += "Case #"+str(n+1)+": Draw\n"


output=output[:-1]
fw = open(namefile+'.out', 'w')
fw.write(output)
fw.close()
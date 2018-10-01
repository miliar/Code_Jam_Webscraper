lines = open('d:\so.txt').read().split('\n')
output = open('d:\output.txt','w')
print(lines)
i = 1
numtest = int(lines[0])

while i <= numtest:
    line = lines[i].split(' ')
    shyhigh = int(line[0])
    aud = list(line[1])
    j=0
    pa=0
    man=0
    
    while j < shyhigh and pa <= shyhigh:
        if aud[j] == '0':
            if( j == 0):
                man += 1
                pa += 1
            else:
                if(pa <= j):
                    man += 1
                    pa += 1
        else:
            pa += int(aud[j])
        j = j + 1
    print('Case #%s: %s' %(i, man))
    output.write('Case #%s: %s\n' %(i, man))
    i = i+1
output.close()
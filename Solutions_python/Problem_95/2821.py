#I/O Setup
with open('ciphers.txt') as ciphers:
    cipher = [line.strip() for line in ciphers]
with open('texts.txt') as texts:
    text = [line.strip() for line in texts]
    
output = open('A-output.txt', 'w')

n = int(cipher[0])
d = dict()

#Solving
for i in range(1, int(n)+1):
    c = cipher[i]
    t = text[i]
    for j in range(len(c)):
        d[c[j]] = t[j]
    d['q'] = 'z'
    d['z'] = 'q'
        
#print d
    
with open('A-input.txt') as ciphers:
    cipher = [line.strip() for line in ciphers]
    
paragraph = ''
for k in range(1, int(cipher[0])+1):
    line = ''
    for l in range(len(cipher[k])):
        line += d[cipher[k][l]]
    paragraph += line
    output.write('Case #{0}: {1}\n'.format(k, line))
    paragraph += '\n'
#print paragraph
output.close()


'''
    for j in range(int(I)):
        for k in range(j+1, int(I)):
            if int(L[j]) + int(L[k]) == C:
                print 'Case #{0}: {1} {2}'.format(i+1, j+1, k+1)
                output.write('Case #{0}: {1} {2}\n'.format(i+1, j+1, k+1))
                break
output.close()
'''
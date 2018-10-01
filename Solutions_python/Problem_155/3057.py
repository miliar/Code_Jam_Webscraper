FIN = open('a.in', 'r')
FOUT = open('a.out', 'w')

for op in range(int(FIN.readline())):
    put = FIN.readline().split()
    max = int(put[0])
    s = put[1]
    up = 0
    res = 0
    for i in range(len(s)):
        if i > up and s[i] != '0':
            res += i - up
            up = i
        up += int(s[i])
    
    
    
    
    
    
    FOUT.write('Case ' + '#' + str(op + 1) + ': ' + str(res) + '\n')
FIN.close()
FOUT.close()
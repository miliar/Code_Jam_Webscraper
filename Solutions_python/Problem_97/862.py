out = ''
line_counter = 0

with open('input/3sample.txt', 'r') as f:
    f.readline()
    
    while 1:
        line = f.readline()
        if not line:
            break
        line_counter += 1
        result = 0
                
        line =  line.split()
        A = int(line[0])
        B = int(line[1])
        
        for n in range(A, B):
            for m in range(n, B+1):
                nStr = str(n)
                mStr = str(m)
                
                if nStr != mStr and nStr.__len__() == mStr.__len__():
                    for i in range(0, nStr.__len__() - 1):
                        nStr = nStr[1:] + nStr[0]
                        if nStr == mStr:
                            result += 1
                            break
        
        out += "Case #" + str(line_counter) + ": " + str(result) + "\n"

fo = open('q3output', "w")
fo.write(out)
fo.close()
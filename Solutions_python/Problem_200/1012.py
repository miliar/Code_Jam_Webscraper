fr = open("input.in", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = int(lines[0].strip())
curTest = 0
curLine = 1

def getLine():
    global curLine
    global lines
    curLine += 1
    return lines[curLine-1]
    
while curTest < numTests:
    num = list(str(getLine().strip()))
    
    
    wrong = -1
    last = int(num[0])
    i = 1
    
    while i < len(num):
        if int(num[i]) < last:
            wrong = i
            break
        last = int(num[i])
        i += 1
        
    if wrong > -1:
        for n in range(wrong, int(len(num))):
            num[n] = "9"
    
        n = wrong-1
        check = int(num[n])
        
        while (n-1) >= 0 and int(num[n-1]) == check:
            num[n] = "9"
            n -= 1
        num[n] = str(int(num[n]) - 1)
        
                    
    fw.write("Case #%d: %d\n" % (curTest+1, int("".join(num))))

    curTest += 1
                    
fr.close()
fw.close()
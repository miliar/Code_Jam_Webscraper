import math

def check(x):
    exam = str(x)
    size = len(exam)
    front = 0
    end = len(exam)-1
    mid = len(exam)/2
    count = 0
    for i in range(front,mid):
        if exam[i] != exam[end]:
            count +=1
            return False
            break
        end -=1
    if count == 0:
        return True

inFile = open('C-small-attempt0.in','r')
outFile = open('codjam2out.txt','w')
filesize = int(inFile.readline())

for a in range(filesize):
    small, big = [int(x) for x in inFile.readline().split(' ')]
    x = int(math.floor(small**0.5))
    y = int(math.floor(big**0.5))+1
    count = 0
    for test in range(x,y):
        if check(test):
            if check(test**2):
                if (test**2>=small) and (test**2 <=big):
                    count += 1
    output = 'Case #'+str(a+1)+': '+str(count)+'\n'
    print 'Case #'+str(a+1)+': '+str(count)
    outFile.write(str(output))

inFile.close()
outFile.close()

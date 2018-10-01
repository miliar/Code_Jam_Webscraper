import math

def getallrec(a):
    grida = []
    answer = [a]
    while (a > 0):
        grida.insert(0,a%10)
        a = a/10
    for i in range(1,len(grida)):
        if(grida[i] != 0):
            newnum = 0
            for j in range(0,len(grida)):
                z = int(math.fmod(i+j,len(grida)))
                newnum = (newnum * 10) + grida[z]
            caninclude = True
            for z in range(0,len(answer)):
                if (newnum == answer[z] or newnum < answer[0]):
                    caninclude = False
            if (caninclude):
                answer.append(newnum)
    answer.pop(0) #Get rid of the original number
    return answer

i = 0
low = []
high = []
IN = open('RecSmallIn.txt','r')
OUT = open('RecSmallOut.txt','w')
for line in IN:
    i = i + 1
    if (i == 1):
        total_cases = int(line)
    else:
        data = line.split(' ')
        low.append(int(data[0]))
        high.append(int(data[1]))

print low
print high
for i in range(0,total_cases):
    answer = 0
    A = low[i]
    B = high[i]
    for x in range(A,B+1):
        for z in getallrec(x):
            if (z >= A and z <= B):
                answer = answer + 1
    print answer
    OUT.write("Case #{0}: {1}\n".format(i+1,answer))
OUT.close()

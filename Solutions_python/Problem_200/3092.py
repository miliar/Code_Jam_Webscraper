import random 

def findTidy(current):
    if(len(current) == 1):
        return current
    
    tidy = 1

    for j in range(1,len(current)):
        if(int(current[j])>=int(current[j-1])):
            tidy+=1


    absoluteTidy = 1
    for j in range(1,len(current)):
        if(int(current[j])>int(current[j-1])):
            absoluteTidy+=1
        
    if(tidy == len(current)):
        answer = str(current)
    else:
        for i in range(0,1):
            temp = findTidy(str(int(current[0:tidy])-1))+"9"*(len(current)-tidy)
            answer = temp

    i = 0
    while(i<len(answer)):
        if(answer[i] == "0"):
            answer = answer[i+1:]
        else:
            break

    return answer

def isTidy(current):
    tidy = 1
    for j in range(1,len(current)):
        if(int(current[j])>=int(current[j-1])):
            tidy+=1

    if(tidy == len(current)):
       return True
    return False

def bruteForce(current):
    for i in range(int(current),0,-1):
        if(isTidy(str(i))):
            return str(i)
    return "1"


f = open("tidy.in","r").read().split("\n")[1:-1]

w = open("tidy.out","w")

for i in range(0,len(f)):
    f[i] = int(f[i])

for r in range(0,len(f)):
    answer = 0

    current = str(f[r])
    answer = findTidy(current)

    w.write("Case #"+str(r+1)+": "+str(answer))
    w.write("\n")

w.close()
    


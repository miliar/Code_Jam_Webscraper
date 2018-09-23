#problemB


def figure(n,k):
    l = [0,n+1]
    lastPersonIndex = 0
    for i in range(k):
        maxi = 0
        index = 0
        for p in range(len(l)-1):
            if maxi < l[p+1] - l[p]:
                maxi = l[p+1] - l[p]
                index = p
        newPerson = (l[index] + l[index+1])//2
        l.insert(index+1,newPerson)
        lastPersonIndex = index+1
    leftS = l[lastPersonIndex] - l[lastPersonIndex-1]-1
    rightS = l[lastPersonIndex+1] - l[lastPersonIndex]-1
    return max(leftS,rightS), min(leftS,rightS)
        

def problem2(fileName):
    f = open(fileName,'r')
    testNum = int( f.readline())


    output = open("Output.txt",'w')
    
    for i in range(testNum):
        s = f.readline().split()
        n,k = int(s[0]),int(s[1])
        res = figure(n,k)
        output.write("Case #"+ str(i+1) +": "+str(res[0]) + " " + str(res[1]))
        output.write("\n")
        
if __name__ == '__main__':
    problem2("C-small-1-attempt0.in.txt")
    print("Complete")

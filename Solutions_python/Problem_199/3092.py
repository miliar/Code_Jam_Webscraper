import sys
sys.setrecursionlimit(2000)

def removeLeadingPancakes(pancakes):
    while(len(pancakes)!=0 and pancakes[0]=='+'):
        pancakes = pancakes[1:]
    return pancakes

def flipFirstPancakes(pancakes, paddle):
    #print("".join(pancakes) + str(paddle))
    for i in range(paddle):
        if(pancakes[i]=='+'):
            pancakes[i]='-'
        else:
            pancakes[i]='+'

def solvePancakes(pancakes, paddle):
    #print("solve: " + "".join(pancakes) + " " + str(paddle))
    pancakes = removeLeadingPancakes(pancakes)
    if(len(pancakes)==0):
        return True, 0
    elif(len(pancakes)<paddle):
        return False, 0
    else:
        flipFirstPancakes(pancakes, paddle)
        status, result = solvePancakes(pancakes, paddle)
        if status==False:
            return False, 0
        else:
            return True, 1+result

t = int(input())
for i in range(1, t + 1):
    pancakes, paddle = input().split(" ")
    paddle = int(paddle)
    status, result = solvePancakes(list(pancakes), paddle)
    if status==False:
        result = "IMPOSSIBLE"
    else:
        result = str(result)
    print("Case #" + str(i) + ": " + result)

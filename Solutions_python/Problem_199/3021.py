cases = int(input())

def isHappy(pancakes):
    for pan in pancakes:
        if pan == '-':
            return False
    return True

for c in range(cases):
    inp = input().split()
    pancakes = list(inp[0])
    k = int(inp[1])
    flips = 0
    if(k > len(pancakes)):
        flips = -1
    else:
        for i in range(len(pancakes)):
            if(len(pancakes) - i == k-1):
                    break
            if(pancakes[i] == '-'):
                flips += 1                
                for j in range(i,k+i):
                    if(pancakes[j] == "+"):
                        pancakes[j] = "-"
                    else:
                        pancakes[j] = "+"
    
    if(isHappy(pancakes)):
        print("Case #{}: {}".format(c+1,flips))
    else:
        print("Case #{}: IMPOSSIBLE".format(c+1))



            

        


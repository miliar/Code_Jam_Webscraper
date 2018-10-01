from sys import stdin

cases = int(stdin.readline())
case = 1

def greaterInd(array):
    greater = array[0]
    index = 0
    for i in range(len(array)):
        if array[i] > greater:
            greater = array[i]
            index = i
    return index
            

for c in range(cases):
    n,k = map(int,stdin.readline().split())
    stalls = [1,n,1]
    while k != 0:
        index = greaterInd(stalls)
        greater = stalls.pop(index)
        if greater % 2 != 0:
            
            maxim = greater//2
            minim = (greater//2)
        elif greater % 2 == 0:
            maxim = greater//2
            minim = (greater//2)-1
        stalls.insert(index,minim)
        stalls.insert(index+1,1)
        stalls.insert(index+2,maxim)
        k -= 1
    print("Case #%d: "%case,end="")
    print(maxim,minim)
    case += 1
    

def parser():
    t = int(raw_input()) 
    cakes = []
    flippers = []
    for i in range(1, t + 1):
        a,b = raw_input().split(" ")
        cakes.append(a)
        flippers.append(int(b))
    return [cakes,flippers]

def findCharPos(str, char):
    return [pos for pos, c in enumerate(str) if char == c]



def allHappy(cakes):
    if (len(cakes) == len(findCharPos(cakes, '+'))):
        return True
    return False

def flipcake(cake, flipper_size, index):
    flip = ""
    res = ""
    for i in range(index, index + flipper_size ):
        if(cake[i] == '-'):
            flip = flip + '+'
        else:
            flip = flip + '-'

    res = cake[0:index]  + flip + cake[(index + flipper_size):]
    return res


def main():
    cakes,flippers = parser()
    for i in range(0,len(cakes)):
        res = solver(cakes[i], flippers[i])
        if (res >= 0) :
            print "Case #" + str(i+1) + ": " +  str(res)
        else : 
            print "Case #" + str(i+1) + ": " + "IMPOSSIBLE"             


def solver(cakes, flipper_size):
    
    if(allHappy(cakes)):
        return 0
    elif(flipper_size > len(cakes)):
        return float('-inf')
    elif (cakes[0] == '-'):
        return solver(flipcake(cakes, flipper_size, 0), flipper_size) + 1

    else :
        return solver(cakes[1::], flipper_size)

if __name__ == "__main__":
    main()
#! python3

def isTidy(x):
    x = str(x)
    isTidy = True
    for i in range (1, len(x)):
        if(x[i] < x[i -1]):
            isTidy = False
            break
        else:
            pass

    return isTidy


t = int(input())
for i in range(1, t + 1):
    n = int(input())

    y = n
    #lastTidy = 0
    while (y >= 0):
        if(isTidy(y)):
            print("Case #{}: {}".format(i, y))
            #lastTidy = y
            break
        else:
            pass

        y = y - 1
        #print (n, lastTidy, isTidy(y), y)

#print("Case #{}: {}".format(i, lastTidy))

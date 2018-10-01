def getTidiest(num):
    l = list(str(num))

    if len(l) == 1:
        return num

    for i in range(len(l)-1, 0, -1):
        if l[i] < l[i-1]:
            l[i-1] = str(int(l[i-1])-1)
            for j in range(i, len(l)):
                l[j] = '9'

    return int(''.join(l))


def isTidy(num):
    l = list(str(num))

    if len(l) == 1:
        return True
    
    for i in range(0, len(l)-1):
        if l[i] > l[i+1]:
            return False

    return True

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {} ".format(i, getTidiest(n)))


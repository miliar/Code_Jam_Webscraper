
def toint(digits):
    num = 0
    maxpow = len(digits)-1
    for i,val in enumerate(digits):
        num += val*10**(maxpow-i)
    return num


def maxtidy(digits):
    itr = 0
    maxdig = -1
    while (itr < len(digits)):
        if digits[itr] >= maxdig:
            maxdig = digits[itr]
            itr += 1
        else:
            break
    if itr == len(digits):
        return toint(digits)
    else:
        for i in range(itr, len(digits)):
            digits[i] = 9
        digits[itr - 1] -= 1
        return maxtidy(digits)


T = int(input())
for i in range(1, T+1):
    num = int(input())
    num = list(map(int, list(str(num))))
    print("Case #{}: {}".format(i, maxtidy(num)))

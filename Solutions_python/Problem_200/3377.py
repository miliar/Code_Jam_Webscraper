#avoloc
def beautify(num):
    digits = []
    inflection = -1
    for c in str(num):
        digits.append(int(c))
        order = len(digits)
        carry = 0
    for i in range(order-1,-1,-1):
        if(carry == 1):
            if(digits[i]==0):
                digits[i] = 9
                carry     = 1
            else:
                digits[i] = digits[i]-1
                carry     = 0
        if(i > 0):
            if(digits[i] < digits[i-1]):
                digits[i] = 9
                carry     = 1
                inflection= i
    if(inflection >= 0):
        for ii in range(inflection,order):
            digits[ii] = 9
    return(int(''.join(map(str,digits))))

t = int(input())
for row in range(1,t+1):
    o = input()
    sol = beautify(o)
    print("Case #{}: {}".format(row,sol))

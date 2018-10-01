def findTidy(number):
    isTidy = True
    digits = list(map(int, list(str(number))))
    for i in range(len(digits)-1,0,-1):
        if digits[i] < digits[i-1]:
            digits[i-1] -= 1
            digits[i] = 9
            isTidy = False
    if isTidy:
        return number
    else:
        return findTidy(''.join(list(map(str, digits))))

def goUp(number, max):
    digits = list(map(int, list(str(number).lstrip("0"))))
    for i in range(len(digits)-1,0,-1):
        while digits[i-1] < digits[i]:
            digits[i-1] += 1
            s = ''.join(list(map(str, digits)))
            n = int(s)
            if n < max:
                continue
            else:
                digits[i-1] -= 1
                break
    return ''.join(list(map(str, digits)))
        
    


numberOfInputs = 0
out = open("output.txt", "w")

with open("B-large.in") as f:
    numberOfInputs = int(f.readline())
    for num in range(1,numberOfInputs +1):
        N = int(f.readline())
        tidy = findTidy(N)
        tidy = goUp(tidy, N)
        out.write("Case #{0}: {1}\n".format(num, tidy))
out.close()


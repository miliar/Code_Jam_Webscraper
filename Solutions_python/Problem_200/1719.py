def ascending(n):
    digits = str(n)
    for i in range(len(digits)-1):
        a = int(digits[i])
        b = int(digits[i+1])
        if b < a:
            return False
    return True

def verifier(n):
    for i in range(n):
        num = n-i
        if ascending(num):
            return num
    return "cant find"

def tidy(n):
    digits = str(n)
    digits_list = [int(x) for x in digits]
    for i in range(len(digits_list)-1):
        a = int(digits_list[i])
        b = int(digits_list[i+1])
        if b < a:
            for j in range(i+1, len(digits_list)):
                digits_list[j] = 9
#            print digits_list
            for j in range(i+1):
                #print digits_list
                ind = i - j
                #print int(digits_list[ind]),a
                if int(digits_list[ind]) == a:
                    if ind > 0:
                        if int(digits_list[ind-1]) == a:
                            digits_list[ind] = 9
                        else:
                            digits_list[ind] -= 1
                    else:
                        digits_list[ind] -= 1
                else:
                    break
            break
    newnew = [str(x) for x in digits_list]
    new = "".join(newnew)
    if new[0] == "0":
        return int(new[1:])
    else:
        return int(new)
        

f = open('a.in', 'r')
g = open('a.out', 'w')

t = int(f.readline())

for i in range(1,t+1):

    #read input
    n  = [int(y) for y in f.readline().split('\n')[0].split(' ')][0]

    #solve
    ans = tidy(n)
    pr = "Case #"+str(i)+ ": " + str(ans)
    #print pr
    g.write(pr + '\n')


f.close()
g.close()

f = open('C:\Users\Arthur\Downloads\C-small-attempt1.in', 'r')
tst = f.readline()

#times = int(raw_input(""))    

def isPal(s):
    def pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and pal(s[1:-1])

    return pal(s)

num={}
if int(tst) >= 1 and int(tst) <= 100:
    for b in range(int(tst)):
        num[b] = 0
        t = f.readline()
        tt = t.split(" ")
        if int(tt[0]) >= 1 and int(tt[1]) >= int(tt[0]) and int(tt[1]) <= 1000:
            for c in range(int(tt[0]), int(tt[1])+1):
                    check = isPal(str(c))
                    if check == True:
                            #print ("palindrom " + str(c))
                            sqrt = c**(1/2.0)
                            if str(sqrt)[-2:] == '.0':
                                    again = isPal(str(int(sqrt)))
                                    if again == True:
                                            num[b] += 1

    for i in num:
        print ("Case #" + str(i+1) + ": " + str(num[i]))

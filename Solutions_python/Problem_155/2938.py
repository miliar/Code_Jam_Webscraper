f = open('C:\Akshay\competitions\codejam\A-large.in', 'r')
f2 = open('C:/Akshay/competitions/codejam/ans2.txt', 'w')

inp = list(f)

temp = inp[0].rsplit()
test = int(temp[0])
w = 1

while w <= test:
    # main code for each program begins here
    temp = inp[w].rsplit()
    smax = int(temp[0])
    a = temp[1]
    ppl = int(a[0])
    i = 1
    friends = 0
    while i <= smax:
        xi = int(a[i])
        if ppl < i:
            friends += i - ppl
            ppl += i - ppl
        ppl += xi
        i+=1
    s = str("Case #" + str(w) + ": " + str(friends))
    # print s
    w += 1
    f2.write(s)
    f2.write("\n")

f2.close()

count = int(raw_input())
for j in range(count):
    L = 0
    R = 0
    inp = raw_input()
    stri, kS = inp.split(' ')
    k = int(kS)
    strT = stri
    res = 0
    for i in range(len(stri) - k + 1):
        if strT[i] =='-':
            res += 1
            flip = strT[i:i+k].replace('+', '1')
            flip = flip.replace('-', '+')
            flip = flip.replace('1', '-')
            strT = strT[0:i] + flip + strT[i+k:len(stri)]
    if strT.find('-') != -1:
        print "Case #" + str(j + 1) +": " + "IMPOSSIBLE"
    else:
        print "Case #" + str(j + 1) +": " + str(res)

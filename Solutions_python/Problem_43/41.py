
T = int(raw_input (""))
for i in range(1,T+1):
    num = str(raw_input(""))
    code = dict ()
    current = 0
    code[num[0]] = 1
    for j in range(1,len(num)):
        if code.get(num[j], None) == None:
            code[num[j]] = current
            if current == 0:
                current = current + 1
            current = current + 1
    if current == 0:
        current = 2
    base = current
    result = 0
    for j in num:
        result = result*base + code[j]
    
    print "Case #%d: %d" % (i, result)

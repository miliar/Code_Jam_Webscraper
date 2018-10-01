for _ in range (input()):
    s = list(raw_input())
    conditionSatisfied = False
    while not conditionSatisfied:
        conditionSatisfied = True
        for i in range(len(s)-1):
            if(int(s[i])>int(s[i+1])):
                b = int(s[i])-1
                s[i] = str(b)
                s[i+1:] = "9"*(len(s)-(i+1))
                conditionSatisfied = False
                break
    s = ''.join(s)
    s = int(s)
    print 'Case #%d:'%(_+1),s


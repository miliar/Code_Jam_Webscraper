num = input()
for ind in range(num):
    case = raw_input().split(" ")
    s, size = [a=="+" for a in case[0]],int(case[1])#Map + to True and - to False
    numFlips = 0
    for i in range(len(s)-size+1):
        if not s[i]:
            numFlips+=1
            for j in range(size):
                s[j+i]= not s[j+i]
    if all(s):#Checks more than it needs to but is easier to think about
        print "Case #%d: %d"%(ind+1,numFlips)
    else:
        print "Case #%d: IMPOSSIBLE"%(ind+1)

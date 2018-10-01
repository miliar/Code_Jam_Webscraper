input = open('A-large.in','r')
#input = open('input2.txt','r')
t = int(input.readline())
for i in range(t):
    (a,n) = input.readline().split()
    a = int(a)
    s = [int(x) for x in input.readline().split()]
    #if a == 1:
    #    continue
    s.sort()
    ret = 0
    #print s
    for (ji,j) in enumerate(s):
        if j < a:
            #print "eat",a,j
            a += j
        elif a-1 > 0:
            temp = 0
            b = a
            while b <=j:
                temp += 1
                #print "add",b,b-1
                b += b-1
            #print "eat",b,j
            if temp > len(s)-ji and len(s)-ji + ret <= len(s):
                #print temp, len(s)-ji
                #print "remove all instead"
                ret += len(s)-ji
                break
            elif temp + ret > len(s):
                #print "remove all all instead"
                ret = len(s)
                break
            else:
                a = b + j
                ret += temp
        else:
            ret += 1
            #print "remove",j
                
    print "Case #"+str(i+1)+": "+str(ret)

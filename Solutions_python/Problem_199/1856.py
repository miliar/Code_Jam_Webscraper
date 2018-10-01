f = file("pancake-output-small.txt","w")
def flip(s,k,start):
    for i in xrange(start,start+k):
        if s[i]=="+":
            s[i]="-"
        else:
            s[i]="+"
    return s

t = int(raw_input())
for case in xrange(1,t+1):
    count = 0
    s,k = raw_input().split()
    s = list(s)
    k = int(k)
    bridge = True
    for i in xrange(len(s)):
        if s[i]=="-" and i>len(s)-k:
            print "Case"+" #"+str(case)+": "+"IMPOSSIBLE"
            f.write("Case"+" #"+str(case)+": "+"IMPOSSIBLE")
            bridge = False
            break

        elif s[i]=="-":
            s = flip(s,k,i)
            count +=1
        #print s
    if bridge:
        print "Case"+" #"+str(case)+": "+str(count)
        f.write("Case" + " #" + str(case) + ": " +str(count))
    f.write("\n")
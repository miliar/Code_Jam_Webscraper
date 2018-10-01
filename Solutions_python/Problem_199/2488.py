def perform(s):
    global count,k
    ind = s.index('-')
    if(ind+k<=len(s)):
        for i in range(ind,ind+k):
            if(s[i]=="-"):
                s[i]="+"
            else:
                s[i]="-"
    else:
        count = "IMPOSSIBLE"
    return s

for _ in range(input()):
    count = 0
    s,k = raw_input().split(" ")
    s = list(s)
    k = int(k)
    while ("-" in s) and type(count) == int:
        count+=1
        s = perform(s)
    print 'Case #%d:'%(_+1),count

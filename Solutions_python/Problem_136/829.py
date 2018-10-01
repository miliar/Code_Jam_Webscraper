T = int(raw_input())
for cases in range(1,T+1):
    l=map(float,raw_input().split())
    c,f,x = l[0],l[1],l[2]
    rate=2
    prevtime=x/rate
    ans=prevtime
    while (prevtime-((x-c)/rate)+(x/(rate+f))) < prevtime:
        #print prevtime
        prevtime = prevtime-((x-c)/rate)+(x/(rate+f))
        ans=prevtime
        rate+=f
    print "Case #" + str(cases) + ": %.7f" %ans

t=int(raw_input())
test=1
while(test<=t):
    c,f,x=map(float,raw_input().split())
    time=float(0.0)
    rate=float(2.0)
    while(1):
        if x/rate < c/rate + x/(rate+f) :
            time+=x/rate
            break
        else:
            time+=c/rate
            rate=rate+f
    print ("Case #"+str(test)+": "+"%.7f"%time )
    test+=1 

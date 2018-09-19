c=int(raw_input())
guardo=""
for i in range(c):
    s=raw_input()
    s=s.split()
    c=float(s[0])
    f=float(s[1])
    x=float(s[2])
    cant_sec=2
    pos_t=[]
    cant_farms=-1
    for _ in range(2):
        cant_farms+=1
        t=0.0
        cant_sec=2.0
        for l in range(cant_farms):
            t+=c/cant_sec
            cant_sec+=f
        pos_t.append(t+x/cant_sec)
    while pos_t[-1]<pos_t[-2]:
        cant_farms+=1
        t=0.0
        cant_sec=2.0
        for l in range(cant_farms):
            t+=c/cant_sec
            cant_sec+=f
        pos_t.append(t+x/cant_sec)
    guardo+= "Case #"+str(i+1)+": "+str(min(pos_t))+"\n"
print guardo 
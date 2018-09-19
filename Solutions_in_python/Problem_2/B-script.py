inp_file=file("B-large.in")
out_file=file("B-large.out","w")

def solve(events):
    events.sort(key=lambda x: x[0]*2+(x[1][1]=="0"))
    na=nb=ma=mb=0
    for event in events:
        if event[1]=="a0":
            na+=1
            if na>ma:ma=na
        elif event[1]=="a1":na-=1
        elif event[1]=="b0":
            nb+=1
            if nb>mb:mb=nb
        elif event[1]=="b1":nb-=1
    return str(ma)+" "+str(mb)

def time2num(time):
    f=time.split(":")
    return int(f[0])*60+int(f[1])

num=int(inp_file.readline())
for case in range(num):
    tt=int(inp_file.readline())
    l1,l2=[int(c1) for c1 in inp_file.readline().split(" ")]
    p=[]
    for line in range(l1):
        t=inp_file.readline().split(" ")
        p.append((time2num(t[0]),"a0"))
        p.append((time2num(t[1])+tt,"b1"))
    for line in range(l2):
        t=inp_file.readline().split(" ")
        p.append((time2num(t[0]),"b0"))
        p.append((time2num(t[1])+tt,"a1"))
    out_file.write("Case #%s: "%(case+1)+solve(p)+"\n")
inp_file.close()
out_file.close()

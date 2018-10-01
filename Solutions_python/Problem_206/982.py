def time(f,t,spd):
    return abs(f-t)/spd

file1=open("a.out","w")
file=open("A (2).in")
T=int(file.readline()[:-1])
for i in range(T):
    lst=file.readline()[:-1].split()
    t=int(lst[0])
    times=[]
    for j in range(int(lst[1])):
        [f,s]=file.readline()[:-1].split()
        f=int(f)
        s=int(s)
        reach=time(f,t,s)
        times.append(reach)
    times.sort()
    file1.write("Case #"+str(i+1)+": "+str(t/times[-1])+"\n")
    times.clear()
file1.close()

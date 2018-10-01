
def run():
    f=open("input.in")
    g=open("out.txt",'w')
    num = int(f.readline())
    for i in range(num):
        g.write("Case #%d: " % (i+1))
        vines = int(f.readline())
        data = [map(int,f.readline().split()) for x in range(vines)]
        goal = int(f.readline())
        possible = False
        if data[0][0]>data[0][1]:
            g.write("NO\n")
            continue
        dists = [0 for x in range(vines)]
        dists[0]=data[0][0]
        newlist = [0]
        while newlist:
            curr = newlist.pop();
            if dists[curr]>= goal-data[curr][0]:
                possible = True
                break
            for j in range(curr+1,vines):
                if data[j][0]<=data[curr][0]+dists[curr]:
                    reach = min(data[j][0]-data[curr][0],data[j][1])
                    if reach>dists[j]:
                        dists[j]=reach
                        newlist.insert(0,j)
        if possible:
            g.write("YES\n")
        else:
            g.write("NO\n")
        continue
    f.close()
    g.close()
    

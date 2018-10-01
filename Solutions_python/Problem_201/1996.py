def count(x,mx,sp):
    indexList = [] 
    for i in range(len(x)):
        if(x[i] == mx and sp[i] == '.'):
            indexList.append(i)
    return indexList
    
def count2(x,mx,sp):
    indexList = [] 
    for i in x.keys():
        if(x[i] == mx):
            indexList.append(i)
    return indexList

def maxi(x,sp):
    xm = -1
    for i in range(len(x)):
        if(xm < x[i] and sp[i] == '.'):
            xm = x[i]
    return xm

fin = open("C:\Users\Harsh Shah\Desktop\in.in","r")
fout = open("C:\Users\Harsh Shah\Desktop\out.txt","w")

t = int(fin.readline())
#t = int(input())
for a in range(t):
    fl = fin.readline().split()    
    n = int(fl[0])
    k = int(fl[1])
    
    #n = int(input())
    #k = int(input())

    s = []
    sp = []
    smin = []
    smax = []
    
    for i in range(n):
        s.append([i,n-(i+1)])
        sp.append('.')
    
    for i in s:
        smin.append(min(i))
        smax.append(max(i))
    
    while(k>0):
        for i in range(len(s)):
            if(sp[i] == '.'):
                smin[i] = (min(s[i]))
                smax[i] = (max(s[i]))
        
        selmin = count(smin,maxi(smin,sp),sp)
        #print selmin
        if(len(selmin) == 1):
            sel = selmin
            sp[sel[0]] = '0'
        else:
            selmax = {}
            for i in selmin:
                selmax[i] = smax[i]
                
            #print selmax
            #selmaxcnt = selmax.values().count(max(selmax.values()))
            sel = sorted(count2(selmax,max(selmax.values()),sp))
            #print sel
            if( len(sel) == 1):
                sp[selmax.keys()[0]] = '0'
            else:
                sp[sel[0]] = '0'
                
        #onLeft
        for i in reversed(range(0,sel[0])):         
            if(i < sel[0] and sp[i] == '.'):
                s[i][1]-=(s[sel[0]][1]+1)
            else:
                break;
        #onRight        
        for i in range(sel[0]+1,n): 
            if(i > sel[0] and sp[i] == '.'):
                s[i][0]-=(s[sel[0]][0]+1)
            else:
                break;
        #print sp
        #print s
        #print smin
        #print smax
        #print "\n"
        k-=1
        
    fout.write("Case #{0}: {1} {2}\n".format(a+1,max(s[sel[0]]),min(s[sel[0]])))
    print("Case #{0}: {1} {2}".format(a+1,max(s[sel[0]]),min(s[sel[0]])))

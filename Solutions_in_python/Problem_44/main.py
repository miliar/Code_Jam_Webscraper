import math

def wf(fileName,ls):
    f = open(fileName,'w')
    for i,l in enumerate(ls):
        f.write('Case #%d: %.8f %.8f\n'%(i+1,l[0],l[1]))
        
def getDis(t,px,py,pz,vx,vy,vz):
    d = (t*vx+px)*(t*vx+px) + (t*vy+py)*(t*vy+py) + (t*vz+pz)*(t*vz+pz)
    return math.sqrt(d)
    
def getTD(lsMass):
    #print 'getTD:',lsMass
    num = len(lsMass)
    px = 0.0
    py = 0.0
    pz = 0.0
    vx = 0.0
    vy = 0.0
    vz = 0.0
    for i in range(num):
        px += lsMass[i][0]
        py += lsMass[i][1]
        pz += lsMass[i][2]
        vx += lsMass[i][3]
        vy += lsMass[i][4]
        vz += lsMass[i][5]
    px = px/num
    py = py/num
    pz = pz/num
    vx = vx/num
    vy = vy/num
    vz = vz/num
    print px,py,pz,vx,vy,vz
    t = (vx*vx+vy*vy+vz*vz)
    if t==0:
        return 0,getDis(0,px,py,pz,vx,vy,vz)
    t = (px*vx+py*vy+pz*vz)/(vx*vx+vy*vy+vz*vz)
    #print t
    if t>0:
        return 0,getDis(0,px,py,pz,vx,vy,vz)
    else:
        t1 = -t
        return t1,getDis(t1,px,py,pz,vx,vy,vz)


filename = 'Sample.in'
filename = 'B-small-attempt2.in'
filename = 'B-large.in'
f = open(filename)
contents = f.readlines()
#print contents
s =contents[0].strip()
n = int(s)
print n
lsResult = []
curPos = 1
for i in range(n):
    print i,'\t:',contents[curPos]
    num = int( contents[curPos].strip() )
    #print num
    curPos += 1
    lsMass = []
    for x in range(num):
        ls = contents[curPos+x].strip().split()
        ls = [float(l) for l in ls]
        lsMass.append(ls)
    #print lsMass
    t,d = getTD(lsMass)        
    curPos += num
    lsResult.append([d,t])
    
    
        
    

#print lsResult

    
wf(filename.split('.')[0]+'.out',lsResult)

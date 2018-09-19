visit=[]

def init():
    for x in range(0,20000):
        visit[x]=0

def length(num):
    count=1
    while True:
        num//=10
        
        if(num==0):
            return count
        count+=1

    
    
def solve(num0,num):
    count=0
    for i in range(num0, num):
        for j in range(0, length(i)-1):
            org=ascii(i)
            buf=org[j+1:]+ org[0:j+1]
            
            org=int(org)
            buf=int(buf)
            #print(org)
            #print(buf)
            #print('===')
            #print(buf)
            if(buf<=num and buf>=num0 and buf>org):
                count+=1
                #print(ascii(org) + " "+ ascii(buf))

    return count

test="""4
1 9
10 40
100 500
1111 2222"""

for x in range(0,20000):
    visit.append(0)


"""
g=[]
for x in k.split("\n"):
    g.append(int(x))

g.sort()
#print(g)
"""
f = open('test.txt', 'r')
test=f.read()

sprite=test.split("\n")
for x in range(0,int(sprite[0])):
    sprite2=sprite[x+1].rstrip().split(" ")
    
    ret=solve(int(sprite2[0]),int(sprite2[1]))
    print("Case #" + ascii(x+1) + ": " + ascii(ret))

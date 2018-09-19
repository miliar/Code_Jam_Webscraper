m = []
h = 0
w = 0
ans = []

def traverse(x,y):
    global m, h, w, ans

    if ans[x][y] != 0:
        return ans[x][y]
    
    no = 99999
    so = 99999
    ea = 99999
    we = 99999
    
    if x != 0:
        no = m[x-1][y]
    if x != h-1:
        so = m[x+1][y]
    if y != 0:
        we = m[x][y-1]
    if y != w-1:
        ea = m[x][y+1]

    a = [m[x][y],no,so,we,ea]
    a.sort()

    b = a[0]
    
    if m[x][y] == b:
        ans[x][y] = (x,y)
        return (x,y)
    elif no == b:
        ans[x][y] = traverse(x-1,y)
        return ans[x][y]
    elif we == b:
        ans[x][y] = traverse(x,y-1)
        return ans[x][y]
    elif ea == b:
        ans[x][y] = traverse(x,y+1)
        return ans[x][y]
    elif so == b:
        ans[x][y] = traverse(x+1,y)
        return ans[x][y]
    
f = open("w.txt","r")
g = open("out.txt","w")

line = f.readline()
t = int(line)

count = 0

while True:
    line = f.readline()
    if not line:
        break

    count += 1
    
    nums = line.split()
    h = int(nums[0])
    w = int(nums[1])

    m = []
    for x in range(h):
        a = f.readline().split()
        for y in range(len(a)):
            a[y] = int(a[y])
        m += [a]

    ans = list()
    for i in xrange(h):
        b = list()
        for j in xrange(w):
            b.append(0)
        ans.append(b)
    
    for x in range(h):
        for y in range(w):
            traverse(x,y)

    g.write("Case #" + str(count) + ":\n")

    d = {}
    c = 97
    for x in ans:
        for y in x:
            if y not in d:
                d[y] = chr(c)
                c += 1
            g.write(d[y] + ' ')
        g.write("\n")

f.close()
g.close()

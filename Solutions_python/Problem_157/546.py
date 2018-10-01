import sys

f = open(sys.argv[1],'r')
o = open(sys.argv[2],'w')

cases = int(f.readline().split()[0])

h = {'i':2,'j':3,'k':4}
arr = [[0,0,0,0,0],[0,1,2,3,4],[0,2,-1,4,-3],[0,3,-4,-1,2],[0,4,3,-2,-1]]

case=1
while case<=cases:
    line = f.readline().split()
    leng = int(line[0])
    n = int(line[1])
    s = f.readline().split()[0]
    ifound = jfound = kfound = False

    x = 1
    pos = True
    for _ in range(n):
        for i in range(leng):
            # get the next state
            x = arr[x][h[s[i]]]
            if x < 0:
                pos = not pos
                x = -x
            if not ifound and x == 2 and pos:
                ifound = True
                x = 1
                pos = True
            if ifound and not jfound and x == 3 and pos:
                jfound = True
                x = 1
                pos = True
            if jfound and not kfound and x == 4 and pos:
                kfound = True
                x = 1
                pos = True
    
    # Successful
    if kfound and x == 1 and pos:
        o.write("Case #{}: YES\n".format(case))
    else:
        o.write("Case #{}: NO\n".format(case))

    case += 1

f.close()
o.close()



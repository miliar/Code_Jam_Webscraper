fin = open('B-small-attempt0.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

colors = ['', 'R', 'O', 'Y', 'G', 'B', 'V']

for i in xrange(t):
    n, r, o, y, g, b, v = map(int, fin.readline().split())

    st = "-"

    while n > 0:
        maxx = 0
        maxxC = ""
        if r > maxx and st[-1] <> 'R':
            maxx = r
            maxxC = "R"
        if y > maxx and st[-1] <> 'Y':
            maxx = y
            maxxC = "Y"
        if b > maxx and st[-1] <> 'B':
            maxx = b
            maxxC = "B"

        if maxx == 0:
            st = "-IMPOSSIBLE"
            break

        n -= 1
        
        if maxxC == "R":
            r -= 1
        elif maxxC == "Y":
            y -= 1
        elif maxxC == "B":
            b -= 1

        st += maxxC

    if len(st) > 3 and st[-1] == st[1]:
        st = st[:-2] + st[-1] + st[-2]
        if st[-2] == st[-3]:
            st = "-IMPOSSIBLE"        
    if len(st) > 2 and st[1] == st[-1]:
        st = "-IMPOSSIBLE"

    print i
      
    fout.write("Case #" + str(i + 1) + ": " + st[1:] + "\n")
fout.close()

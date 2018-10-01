import sys

#f = open('B-small1.in', 'r')
f = open('B-large.in', 'r')
i = 0
cur_case = 0
for line in f:
    if i == 0:
        t = line
        i = i + 1
        continue
    else:
        cur_case = cur_case + 1
    c = {}
    o = {}
    e = []
    oo = []
    els = str.split(line)
    nc = int(els[0])
    s = 1
    cur = nc + 1
    if nc > 0:
        for i in range(s,cur):
            c[els[i][0] + els[i][1]] = els[i][2]
            c[els[i][1] + els[i][0]] = els[i][2]
    no = int(els[cur])
    s = cur + 1
    cur = s + no
    if no > 0:
        for i in range(s,cur):
            o[els[i][0] + els[i][1]] = 1
            o[els[i][1] + els[i][0]] = 1
    #print c
    #print o
    #print els[cur+1]
    for a in els[cur+1]:
        #print "oo:" + str(oo)
        #print e
        e.append(a)
        if len(e) > 1:
            two = e[-1] + e[-2]
            if two in c:
                e.pop()
                oo.pop()
                e[-1] = c[two]
            else:
                cl = False
                for t in oo:
                    key = t + a
                    if key in o:
                        cl = True
                        break
                if cl:
                    e = []
                    oo = []
                else:
                    oo.append(a)
        else:
            oo.append(a)
    print "Case #" + str(cur_case) + ": " + "[" + ", ".join(e) + "]"
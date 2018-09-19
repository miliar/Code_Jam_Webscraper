def find(li, idx, type):
    while idx < len(li):
        if type == li[idx]:
            return idx
        idx += 1
    return None

def next_pos(pos, tick, onward):
    if tick < abs(pos - onward):
        if pos > onward:
            pos -= tick
        else:
            pos += tick
    else:
        pos = onward
    return pos

def solve(n, robot, buttom):
    #print locals()
    time = 0
    op = 1
    bp = 1
    o = -1
    b = -1
    onx = True
    bnx = True
    while o != None or b != None:
        tick = 0
        if o != None and onx:
            old = o
            o = find(robot, o + 1, "O")
            onx = False
        if b != None and bnx:
            old = b
            b = find(robot, b + 1, "B")
            bnx = False

        if (o != None and b != None and o < b) or (o != None and b == None):
            #print "push orange"
            onx = True
            if buttom[o] != op:
                tick = abs(buttom[o] - op) + 1
                op = buttom[o]
            else:
                tick = 1
            if b != None:
                bp = next_pos(bp, tick, buttom[b])
        elif (o != None and b != None and o > b) or (o == None and b != None):
            #print "push blue"
            bnx = True
            if buttom[b] != bp:
                tick = abs(buttom[b] - bp) + 1
                bp = buttom[b]
            else:
                tick = 1
            if o != None:
                op = next_pos(op, tick, buttom[o])
        time += tick
        #print "###{0}: ".format(time),
        #print "orange -> {0}, ({1}, {2}), ".format(op, o, buttom[o] if o != None else "None"),
        #print "blue -> {0}, ({1}, {2}) ".format(bp, b, buttom[b] if b != None else "None")
    return time

t = int(raw_input())
for i in xrange(t):
    x = raw_input().split()
    n = int(x[0])
    rp = x[1:]
    robot = []
    buttom = []
    for k in xrange(0, len(rp), 2):
        robot.append(rp[k])
        buttom.append(int(rp[k+1]))
    r = solve(n, robot, buttom)
    print "Case #{0}: {1}".format(i + 1, r)

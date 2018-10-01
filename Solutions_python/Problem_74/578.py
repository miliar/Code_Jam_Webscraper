def solve(osteps, bsteps):
    time = 0
    ostep = bstep = None
    if len(osteps) > 0:
        ostep = osteps.pop(0)
    if len(bsteps) > 0:
        bstep = bsteps.pop(0)
    opos, bpos = 1, 1
    while ostep or bstep:
        if not bstep or ostep and ostep[0] < bstep[0]:
            # +1 for button push
            move = abs(ostep[1] - opos) + 1
            time += move
            opos = ostep[1]

            if len(osteps) > 0:
                ostep = osteps.pop(0)
            else:
                ostep = None

            if not bstep:
                continue
            if bpos > bstep[1]:
                bpos = max(bpos - move, bstep[1])
            elif bpos < bstep[1]:
                bpos = min(bpos + move, bstep[1])
        else:
            # +1 for button push
            move = abs(bstep[1] - bpos) + 1
            time += move
            bpos = bstep[1]

            if len(bsteps) > 0:
                bstep = bsteps.pop(0)
            else:
                bstep = None

            if not ostep:
                continue
            if opos > ostep[1]:
                opos = max(opos - move, ostep[1])
            elif opos < ostep[1]:
                opos = min(opos + move, ostep[1])
    return time

t = int(input())
for case in range(t):
    line = input().split(' ')
    n = int(line.pop(0))
    osteps, bsteps = [], []
    for step in range(n):
        r, p = line[0], int(line[1])
        line = line[2:]
        if r == 'O':
            osteps.append((step, p))
        else:
            bsteps.append((step, p))
    #print(osteps, bsteps)
    print("Case #%d:" % (case+1), solve(osteps, bsteps))


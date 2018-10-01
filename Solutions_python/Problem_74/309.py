import sys
si = sys.stdin

T = int(si.readline())

def findGoal(t, commands, from_index):
    for i, c in enumerate(commands[from_index:]):
        if (c[0] == t):
            return (i + from_index, c[1])
    return (-1, -1)

for tcase in range(T):
    line = si.readline()
    tokens = line.split()
    N = int(tokens[0])
    commands = [(tokens[1+2*i], int(tokens[2+2*i])) for i in range(N)]

    #print "Tokens:", tokens
    #print commands

    time_steps = 0
    
    upto_command = 0
    opos = 1
    bpos = 1
    ogoal = findGoal('O', commands, 0)
    bgoal = findGoal('B', commands, 0)
    #print "ogoal", ogoal, bgoal

    while upto_command < len(commands):
        block = False
        if opos < ogoal[1]:
            opos += 1
        elif opos > ogoal[1]:
            opos -= 1
        elif upto_command == ogoal[0]:
            #Push button.
            upto_command += 1
            ogoal = findGoal('O', commands, upto_command)
            block = True
            
        if bpos < bgoal[1]:
            bpos += 1
        elif bpos > bgoal[1]:
            bpos -= 1
        elif upto_command == bgoal[0] and not block:
            upto_command += 1
            bgoal = findGoal('B', commands, upto_command)

        time_steps += 1

    print "Case #%d: %d" % (tcase+1, time_steps)

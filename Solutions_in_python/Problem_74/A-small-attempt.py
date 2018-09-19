fin = open ('A-small-attempt0.in', 'r')
fout = open('A-small-attempt0.out', 'w')

cases = fin.readline()
index = 0

for line in fin:
    index += 1
    steps = line.split()

    #don't need the first step (number of steps)
    steps.pop(0)

    all_steps = []
    o_steps = []
    b_steps = []

    #get steps in case    
    while len(steps) > 0:
        bot = steps.pop(0)
        num = steps.pop(0)

        if bot == 'O':
            o_steps.append(int(num))
        elif bot == 'B':
            b_steps.append(int(num))

        all_steps.append(bot)
        all_steps.append(int(num))

    o_pos = 1
    b_pos = 1

    seconds = 0

    goal_bot = all_steps.pop(0)
    goal_pos = all_steps.pop(0)

    print "Time | Orange           | Blue"
    print "-----+------------------+-----------------"

    while goal_pos:
        seconds += 1

        pstr = "  " + str(seconds) + "  | "
        
        if len(o_steps) == 0:
            pstr += "Stay at button   | "
        elif o_pos < o_steps[0]:
            pstr += "Move to button " + str(o_steps[0]) + " | "
            o_pos += 1
        elif o_pos > o_steps[0]:
            pstr += "Move to button " + str(o_steps[0]) + " | "
            o_pos -= 1
        elif o_pos == o_steps[0]:
            if goal_bot == 'O':
                pstr += "Push button " + str(o_steps[0]) + "    | "
                o_steps.pop(0)
                pushed = 1
            else:
                pstr += "Stay at button " + str(o_steps[0]) + " | "

        if len(b_steps) == 0:
            pstr += "Stay at button"
        elif b_pos < b_steps[0]:
            pstr += "Move to button " + str(b_steps[0])
            b_pos += 1
        elif b_pos > b_steps[0]:
            pstr += "Move to button " + str(b_steps[0])
            b_pos -= 1
        elif b_pos == b_steps[0]:
            if goal_bot == 'B' and pushed == 0:
                pstr += "Push button " + str(b_steps[0])
                b_steps.pop(0)
                pushed = 1
            else:
                pstr += "Stay at button " + str(b_steps[0])

        if pushed:
            pushed = 0
            if len(all_steps) > 0:
                goal_bot = all_steps.pop(0)
                goal_pos = all_steps.pop(0)
            else:
                goal_pos = 0

        print pstr

    print str(seconds) + " total seconds"
    fout.write("Case #%d : %d\n" % (index, seconds))

fout.close()
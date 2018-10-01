# Google code jam
# Carlos Amedee
# round 1
# bot trust

import sys

class spot(object):
    def __init__(self, player, spot):
        self.player = player
        self.spot = spot

in_file = open(sys.argv[1], 'r')
out_file = open("results.txt", 'w')

cases = in_file.readline().strip()

for case in range(0, int(cases)):
    next_move = 0
    blue_q = []
    orange_q = []
    general_q = []
    case_str = in_file.readline().strip()
    case_arr = case_str.split(" ")
    button_count = case_arr[0]
    case_arr.pop(0)
    for move in range(0, int(button_count)):
        if case_arr[0] == "O":
            orange_q.append(int(case_arr[1]))
        else:
            blue_q.append(int(case_arr[1]))
        general_q.append(spot(case_arr[0], int(case_arr[1])))
        case_arr.pop(0)
        case_arr.pop(0)
    
    time = 0
    b = 1
    o = 1
    
    while len(general_q) > 0:
        increment = False
        if len(blue_q) > 0:
            if b != blue_q[0]:
                if blue_q[0] > b:
                    b+=1
                else:
                    b-=1
            else:
                if general_q[0].player == "B":
                    blue_q.pop(0)
                    increment = True

        if len(orange_q) > 0:
            if o != orange_q[0]:
                if orange_q[0] > o:
                    o+=1
                else:
                    o-=1
            else:
                if general_q[0].player == "O":
                    orange_q.pop(0)
                    increment = True
        if increment:
            general_q.pop(0)
        time+=1

    print "Case #%d: %d" % (case+1, time)
    output = "Case #%d: %d" % (case+1, time)
    
    out_file.write(output + "\n")
    #out_file.close()
    

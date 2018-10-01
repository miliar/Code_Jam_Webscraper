#!/usr/bin/python
import re

#Read input
f       = open('inp.txt', 'r')
lines   = f.readlines()
f.close()

#Output
f       = open('out.txt', 'w')
total   = lines.pop(0)
c       = 0

debug   = False

while(True):
    if len(lines) == 0:
        break

    listn  = lines.pop(0)
    c   += 1
    listn.rstrip('\n')
    listn = listn.split(" ")
    total = listn.pop(0);

    # collect into separate list
    o_list = []
    b_list = []
    o_pos  = 1
    b_pos  = 1
        
    curr_o = True

    index = 0
    
    while(index < len(listn)):
        item = listn[index]
        index += 1
        if item == "O":
            curr_o = True
        elif item == "B":
            curr_o = False
        else:
            if (curr_o):
                o_list.append(int(item))
            else:
                b_list.append(int(item))

    new = True
    count = 1
    moves = []
    curr = 0
    for each in listn:
        if count % 2 == 0:
            moves[curr].append(int(each))
            curr+=1
        else:
            moves.append([each])
    
        count +=1

    if debug:
        print moves
    # now we have move for each o or b
    # note it cannot push at same time, otherwise it's freely move
    time = 0
    cont = True
    
    curr_step = 0
    while(cont):

        each = moves[curr_step]
        curr_move_item = each[0]
        curr_move_pos  = each[1]

        # Both are at its position
        if curr_move_item == 'O':
            # at O
            if (curr_move_pos == o_list[0]) and (curr_move_pos == o_pos):  #if it needs to push
                button = o_list.pop(0)
                curr_step += 1  # next step
                if debug:
                    print "o pushs "+str(button),

            #at O, no push, so move O
            else:
                if len(o_list) > 0:
                    if (o_pos < curr_move_pos):
                        o_pos += 1
                    elif (o_pos > curr_move_pos):
                        o_pos -= 1
                    if debug:
                        print  "o moves to "+str(o_pos),
                else:
                    if debug:
                        print  "o stays at "+str(o_pos),

            #at O, does b stay or move?
            if len(b_list) > 0:
                if b_pos < b_list[0]:
                    b_pos += 1
                elif b_pos > b_list[0]:
                    b_pos -= 1
                if debug:
                    print "b moves to "+str(b_pos)
            else:
                if debug:
                    print "b stays at "+str(b_pos)

        elif curr_move_item == 'B':
            # at B
            if (curr_move_pos == b_list[0]) and (curr_move_pos == b_pos):  
                button = b_list.pop(0)
                curr_step += 1  # next step
                if debug:
                    print "b pushs at "+str(button),
            #at B, no push, so move B          
            else:
                if len(b_list) > 0:
                    if (b_pos < curr_move_pos):
                        b_pos += 1
                    elif (b_pos > curr_move_pos):
                        b_pos -= 1
                    if debug:
                        print  "b moves to "+str(b_pos),
                else:
                    if debug:
                        print  "b stays at "+str(b_pos),

            #at B, does O stay or move?
            if len(o_list) > 0:
                if o_pos < o_list[0]:
                    o_pos += 1
                elif o_pos > o_list[0]:
                    o_pos -= 1
                if debug:
                    print "o moves to "+str(o_pos)
            else:
                if debug:
                    print "o stays at "+str(o_pos)

        time += 1
        if len(o_list) == 0 and len(b_list) == 0:
            cont = False

        #print str(b_list) + " " + str(o_list)

    if debug:
        print time
    output = "Case #"+str(c)+": "+str(time)
    print output
    output += "\n"
    #break
    f.write(output)
f.close()

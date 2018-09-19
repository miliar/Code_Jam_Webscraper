lines = open("A-large.in", "r").readlines()
out_file = open("codejam1_largeoutput.out", "w")
for i, line in enumerate(lines[1:]):
	if len(line) > 2:
		out_file.write("Case #" + str(i+1) + ": " + str(process_instructions(line)) + "\n")
out_file.close()	
def process_instructions(instructions_string):
    instructions = instructions_string.split()
    robot_sequence = [instruction for instruction in instructions if instruction=='O' or instruction=='B']
    current_robot_index = 0
    o_buttons = [int(instruction) for i, instruction in enumerate(instructions) if instructions[i-1]=='O']
    o_button_index = 0
    b_buttons = [int(instruction) for i, instruction in enumerate(instructions) if instructions[i-1]=='B']
    b_button_index = 0
    o_position = 1
    b_position = 1
    pressed_button_count = 0
    seconds = 0
    while True:
        button_pressed_this_turn = False
        #print "Robot's turn:", robot_sequence[current_robot_index]
        seconds += 1
        #print "On second", seconds
        # do a lot of stuff here, break if we press all the buttons
        if o_button_index < len(o_buttons):
            # We still have buttons left to press
            # a safe action on any given second is to move closer to the next button
            #print "Robot O is seeking button", o_buttons[o_button_index]
            if o_position != o_buttons[o_button_index]:
                # On this turn, robot O is just going to move towards its next button
                if o_position < o_buttons[o_button_index]:
                    o_position += 1
                    #print "Robot O moves to position", o_position
                else:
                    o_position -= 1
                    #print "Robot O moves to position", o_position
            else:
                # Robot O is at its next button, ready to press the button. If it's robot O's turn,
                # press the button. Otherwise, wait. 
                if robot_sequence[current_robot_index] == 'O' and not button_pressed_this_turn:
                    #print "Robot O presses button", o_position
                    button_pressed_this_turn = True
                    current_robot_index += 1
                    if current_robot_index == len(robot_sequence):
                        # We've run out of button pressing instructions, we're done
                        break
                    o_button_index += 1
                #else:
                    #print "Robot O is waiting"
        #else:
            #print "Robot O has run out of buttons to press."
        if b_button_index < len(b_buttons):
            # We still have buttons left to press
            # a safe action on any given second is to move closer to the next button
            #print "Robot B is seeking button", b_buttons[b_button_index]
            if b_position != b_buttons[b_button_index]:
                # On this turn, robot B is just going to move towards its next button
                if b_position < b_buttons[b_button_index]:
                    b_position += 1
                    #print "Robot B moves to position", b_position
                else:
                    b_position -= 1
                    #print "Robot B moves to position", b_position
            else:
                # Robot B is at its next button, ready to press the button. If it's robot B's turn,
                # press the button. Otherwise, wait. 
                if robot_sequence[current_robot_index] == 'B' and not button_pressed_this_turn:
                    #print "Robot B presses button", b_position
                    button_pressed_this_turn = True
                    current_robot_index += 1
                    if current_robot_index == len(robot_sequence):
                        # We've run out of button pressing instructions, we're done
                        break
                    b_button_index += 1
                #else:
                    #print "Robot B is waiting"
        #else:
            #print "Robot B has run out of buttons to press."
    return seconds            

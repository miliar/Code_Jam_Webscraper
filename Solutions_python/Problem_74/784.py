#!/usr/bin/env python

input_file = 'bots-large.dat'

class robot:
    def __init__(self, color, targets):
        self.color = color
        self.position = 1
        self.waiting = True
        self.target_list = targets
        if (targets):
            self.target_next = int(self.target_list.pop(0))
        else:
            self.target_next = 1
        
    def move(self):
        if (self.position < self.target_next):
            self.position += 1
            return 0
        elif (self.position > self.target_next):
            self.position -= 1
            return 0
        elif (self.position == self.target_next):
            if(self.waiting):
                # Do nothing
                return 0
            else:
                # Push the button and move on
                try:
                    self.target_next = int(self.target_list.pop(0))
                    return 1
                except IndexError:
                    # If the list is empty, then we're done
                    return 2
                
    def __repr__(self):
        rep_str = self.color + ": " + str(self.position) + " --> " + str(self.target_next)
        return rep_str

with open (input_file, 'r') as data_file:
    N_tests = int(data_file.readline())
    test_case = data_file.readline()
    test_counter = 0
    while(test_case):
        test_counter += 1
        test_list = test_case.split()
        N_moves = int(test_list.pop(0))
        
        # Sanity check
        assert len(test_list) == 2*N_moves

        test_sequence = []
        test_buttons = {'O': [], 'B': []}

        for x in test_list:
            if(x == 'O' or x == 'B'):
                color = x
                test_sequence.append(x)
                next
            else:
                test_buttons[color].append(x)
        
        # Time for science        
        p_body = robot('O', test_buttons['O'])
        atlas = robot('B', test_buttons['B'])
        bots = {'O': p_body, 'B': atlas }

        move_count = 0

        for color in test_sequence:
            bots[color].waiting = False     # Get a move on
            pushed = 0
            while(not pushed):
                for bot in bots.values():
#                    print bot
                    pushed += bot.move()
                move_count += 1
 
            bots[color].waiting = True
            if (pushed == 2):
                # Our bot is out of instructions, so terminate
                del bots[color]
    
            
        print "Case #%d: %d" % (test_counter, move_count)
        test_case = data_file.readline()


    
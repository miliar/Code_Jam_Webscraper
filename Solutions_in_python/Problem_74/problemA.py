# -*- coding: utf-8 -*-

DEBUG_LEVEL = 0

def debug( lvl, msg ):
    if DEBUG_LEVEL >= lvl:
        print 'debug(%d): %s' % (lvl, msg)

from codejam import read_params

def distance( a, b ):
    """ Calculate unit distance between two buttons. """
    return abs(a - b)


def other( agent ):
    """ Give index of the other agent """
    return (agent + 1) % 2

def calc_move_times( buttons ):
    """ Calculate and return total move times, given as a list of buttons as ( agent#, button# ) tuples ) """
    movetime = [ 0, 0 ]
    position = [ 1, 1 ]  # Initial starting position - each agent at button 1
    total_time = 0

    for (agent, target) in buttons:
        dist = distance( position[agent], target )  # distance to travel to reach target
        time = dist - movetime[agent]               # how much additional time this will take
        if time < 0:
            time = 0

        debug( 2, "agent: %d, target: %3d, dist: %3d, time: %3d" % (agent, target, dist, time) )
        movetime[agent] = 0                         # (we've used up our extra time given by the other agent)
        position[agent] = target                    # but we're at the target

        total_time += time + 1                      # time to move + 1 for button press
        movetime[other(agent)] += time + 1          # give the time expended to the other agent to move

    # If we've processed all the buttons, we're done
    return total_time


# read_input: Read one test case's worth..
def read_input( infile ):
    points = []
    params = read_params( infile )

    buttons = []

    # Read the list of moves in
    num_buttons = params[0] # ignored
    params = params[1:]
    while params:
        if params[0] == 'O':
            agent = 0
        elif params[0] == 'B':
            agent = 1
        else:
            raise Exception, "Unexpected Agent Input Encountered!"

        # Note: this should throw an exception if an integer isn't next
        button_num = int( params[1] )
        
        buttons.append( ( agent, button_num ) )
        params = params[2:]

    num_moves = calc_move_times( buttons )
    
    return num_moves


def runner( infile, debuglvl=0 ):
    global DEBUG_LEVEL
    DEBUG_LEVEL = debuglvl
    
    moves = read_input( infile )
    
    debug( 1, "Number of moves: %s" % (moves,) )
    
    return moves

"""Problem A. Oversized Pancake Flipper"""

import re
from collections import deque

def flip(cake):
    """flip the cake"""
    if cake == "+":
        return "-"
    else:
        return "+"

def flip_k_cakes(cakes, k, index):
    """flip the k cakes starting at index"""
    flippedcakes = ""
    for j, cake in enumerate(cakes):
        if index <= j < (index + k):
            flippedcakes += flip(cake)
        else:
            flippedcakes += cake
    return flippedcakes

def contains_griddle_state(griddle_states_list, potential_flip):
    """find the griddle state in the list"""
    for g_s in griddle_states_list:
        if g_s.pancakes == potential_flip:
            return True
    return False

# fix this to find state with fewest flips
def find_with_fewest_flips(seek_state, state_list):
    """find the seek_state-matching griddle state in the given state_list with the fewest flips"""
    possible = []
    for item in state_list:
        if item.pancakes == seek_state.pancakes:
            possible.append(item)
    if len(possible) > 0:
        possible.sort(key=lambda s: s.flips)
        return possible[0]
    else:
        return None

def generate_states(start_state, flip_size):
    """given a state and a flipper size, return a list of next states"""
    pstates = []
    for index in range(0, len(start_state.pancakes) - flip_size + 1):
        pstate = GriddleState(flip_k_cakes(start_state.pancakes, K, index), start_state.flips + 1)
        pstates.append(pstate)
    return pstates

class GriddleState:
    """A state of the griddle"""
    def __init__(self, pancakes, flips):
        self.pancakes = pancakes
        self.flips = int(flips)

griddle_states = deque() # [a-z_][a-z0-9_]{2,30}$ ??
potential_states = deque()

PLUSES = re.compile(r"^\+*$") # pattern of all pluses... so happy!
MINUSES = re.compile(r"^-*$") # pattern of all minuses... lame

T = int(input())  # get number of test cases
for i in range(1, T + 1):   # loop over the test cases
    t = input().split(" ")  # read a test case
    S = t[0] # pancake string
    K = int(t[1]) # flipper size

    # stick S on the stack with 0 flips
    state = GriddleState(S, 0)
    griddle_states.append(state)

    if not PLUSES.match(state.pancakes):
        # generate potential states and add to potential states list
        potential_states.extend(generate_states(state, K))

        while len(potential_states) > 0:
            curr_pstate = potential_states.popleft()
            # if not visited at a lower level
            if not find_with_fewest_flips(curr_pstate, griddle_states):
                griddle_states.append(curr_pstate)
                potential_states.extend(generate_states(curr_pstate, K))

    plus_state = GriddleState("+" * len(S), 0)
    happy_state = find_with_fewest_flips(plus_state, griddle_states)
    if happy_state:
        print("Case #{}: {}".format(i, happy_state.flips))
        #print("{} {} | Test: {}".format(S, K, happy_state.flips))
    else:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))
        #print("{} {} | Test: {}".format(S, K, "IMPOSSIBLE"))

    griddle_states.clear()

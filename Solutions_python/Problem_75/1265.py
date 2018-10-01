#!/usr/bin/env python
import sys

case = 1

def init():
    global spell_stack
    global oppositions
    global combinations
    combinations = {}
    oppositions = {}
    spell_stack = []

def combination(one, two):
    global combinations
    return (combinations.get(one + two, None) or combinations.get(two + one, None))

def opposes(one, two):
    global oppositions
    return (oppositions.get(one, None) == two or oppositions.get(two, None) == one)

def add_combination(one, two, three):
    global combinations
    combinations[one + two] = three
    combinations[two + one] = three

def add_opposition(one, two):
    global oppositions
    oppositions[one] = two
    oppositions[two] = one

def invoke(invocation):
    # Nothing on the stack
    global spell_stack
    if len(spell_stack) == 0:
        spell_stack.append(invocation)
        return

    # Handle combinations
    comb = combination(invocation, spell_stack[-1])
    if comb:
        spell_stack.pop()
        spell_stack.append(comb)
        return

    # Handle oppositions
    for spell in spell_stack:
        if opposes(invocation, spell):
            spell_stack = []
            return

    spell_stack.append(invocation)

def invoke_chain(chain):
    global case
    for link in chain:
        invoke(link)
    print "Case #" + str(case) + ": [" + ", ".join(spell_stack) + "]"
    case = case + 1

# States:
# 0: Empty
# 1: Reading combinations
# 2: Reading oppositions
# 3: Reading invocations

if __name__ == "__main__":
    init()
    infile = sys.argv[1]
    with open(infile) as f:
        lines = f.readlines()

    lines = lines[1:]

    for line in lines:
        state = 0
        params = line.split()

        for param in params:
            foo = None
            try:
                foo = int(param)
            except ValueError:
                if state == 1:
                    add_combination(param[0], param[1], param[2])
                if state == 2:
                    add_opposition(param[0], param[1])
                if state == 3:
                    invoke_chain(param)
                    init()
            if foo is not None:
                state = state + 1

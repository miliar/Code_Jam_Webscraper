import fileinput


def main():
    """Flip some pancakes"""
    cases = []
    case_counter=0
    for line in fileinput.input():
        if fileinput.isfirstline():
            num_cases=line.strip()
        else:
            case_counter = case_counter + 1
            pancake_state, flipper_size = line.strip().split(" ")
            cases.append( (case_counter, pancake_state, int(flipper_size)) )


    for case in cases:
        calc_case(*case)


def all_happy(pancake_state):
    return pancake_state.count("+") == len(pancake_state)

def range_happy(pancake_state, position, flipper_size):
    if position+flipper_size <= len(pancake_state):
        return pancake_state[position:position+flipper_size].count("+") == flipper_size
    else:
        raise ValueError ("Range Check of %s len %d at pos %d with flipper %d is illegal" % (pancake_state, len(pancake_state), position, flipper_size))

def breadth_based_calculate(pancake_state, flipper_size, current_count, seen_before):
    if all_happy(pancake_state):
        return current_count
    else:
        this_stage = [(current_count,pancake_state, seen_before)]
        new_results=[]
        min_result=-1
        seen_vals = set()
        while this_stage:
            (move_num, state_so_far, seen_this)  = this_stage.pop(0)
            if state_so_far not in seen_vals:
                seen_vals.add(state_so_far)
                for testflip in range(0,len(state_so_far)-flipper_size+1):
                    #No need to flip all +s
                    if not(range_happy(state_so_far,testflip,flipper_size)):
                        new_state = flip_range(state_so_far,testflip,flipper_size)
                        #First answer is OK!
                        if all_happy(new_state):
                            return move_num+1
                        if new_state not in seen_this:
                            seen_this_new = seen_this.copy()
                            seen_this_new.add(new_state)
                            this_stage.append( (move_num+1,new_state, seen_this_new) )
        return -1


def calc_case(case_num, pancake_state, flipper_size):
    #print case_num, pancake_state, flipper_size

    #Early exit if we're done
    if all_happy(pancake_state):
        print "Case #%d: 0" % (case_num, )
    else:
        seen=set()
        seen.add(pancake_state)
        result= breadth_based_calculate(pancake_state,flipper_size,0,seen)
        if result<0:
            print "Case #%d: %s" % (case_num, "IMPOSSIBLE",)
        else:
            print "Case #%d: %d" % (case_num, result,)

def flip_range(pancake_state, position, flipper_size):
    if position+flipper_size <= len(pancake_state):
        return pancake_state[:position]+ flip_chars(pancake_state[position:position+flipper_size])+pancake_state[position+flipper_size:]
    else:
        raise ValueError ("Flip of %s len %d at pos %d with flipper %d is illegal" % (pancake_state, len(pancake_state), position, flipper_size))


def flip_chars(pancake_state):
    return "".join(map(lambda v: '+' if v == '-' else '-', pancake_state))

if __name__ == '__main__':
    main()

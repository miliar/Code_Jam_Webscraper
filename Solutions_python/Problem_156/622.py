#!/usr/bin/env python
import math

def max_cuts(stack_size):
    if stack_size < 2:
        return 0

    x = math.sqrt(stack_size)
    xf = int(math.floor(x))

    if x == xf:
        return xf-1
    return xf

def after_cut(stack_size, ct, cuts):
    return int(math.ceil(stack_size / (cuts+1.0)))

with open('B-large.in') as f:
    cases = int(f.readline())

    for caseNum in range(1, cases+1):
        D = int(f.readline())
        plates = [int(s) for s in f.readline().split()]
        
        stacks = [(s, plates.count(s)) for s in sorted(list(set(plates)), reverse=True)]

        """
        Without splitting any stacks it will take the number of
        minutes equal to pancakes in the first stack
        """
        max_height = stacks[0][0]
        max_time = max_height
        
        """
        Starting from a max height of 0, find the minimum number
        of minutes to obtain this height
        """
        for mh in range(0, max_height):
            #print("---> Checking max height={0}".format(mh))
            time = 0
            mh_actual = 0
            valid = True

            for s in stacks:
                stack_size = s[0]
                stack_ct = s[1]

                if stack_size < mh:
                    if stack_size > mh_actual:
                        mh_actual = stack_size
                    continue

                cut_limit = max_cuts(stack_size)
                found = False

                for cuts in range(0, cut_limit+1):
                    new_height = after_cut(stack_size, stack_ct, cuts)
                    #print("New height: {0} after {1} cuts. mh={2}".format(new_height, cuts, mh))
                    if new_height <= mh:
                        #print("Selecting cut")
                        if new_height > mh_actual:
                            mh_actual = new_height
                        time += stack_ct * cuts
                        found = True
                        break

                if not found or (time + mh_actual) > max_time:
                    valid = False
                    #print("Dying...")
                    break

            if valid and (time + mh_actual) <= max_time:
                #print("Update max time: {0}".format(time))
                max_time = time + mh_actual

        print("Case #{0}: {1}".format(caseNum, max_time))

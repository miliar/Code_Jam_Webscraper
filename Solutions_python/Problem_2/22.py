"""started 11h30

"""

from math import sqrt
import datetime

import psyco
psyco.full()

_debug = 0


class my_action_c:
    def __init__(self, where, time, is_arrival):
        self.where = where # "A" or "B"
        self.time = time   # time object
        self.is_arrival = is_arrival  # bool

    def __str__(self):
        if self.is_arrival:
            what_str = "arrival in"
        else:
            what_str = "departure from"
        return "%s : %s %s" % (self.time.strftime("%H:%M"),
                               what_str,
                               self.where)

def get_time(time_str):
    h, m = [int(item) for item in time_str.split(":")]
    return datetime.datetime(1940, 1, 1, h, m)



def f_sort(a1, a2):

    if a1.time > a2.time:
        return 1

    elif a1.time < a2.time:
        return -1

    else: # Times are equal, make the arrival first
        if a1.is_arrival and not a2.is_arrival:
            return -1
        elif not a1.is_arrival and a2.is_arrival:
            return 1
        else:
            return 0

def algo_complete(turnaround, a2b_l, b2a_l):

    time_turnaround = datetime.timedelta(seconds = 60 * turnaround)
    
    actions_l = []


    # Put all in a list
    for time_from_a, time_to_b in a2b_l:
        #departure
        actions_l.append(my_action_c("A", time_from_a, is_arrival = False))

        #arrival (and ready for next departure)
        actions_l.append(my_action_c("B", time_to_b + time_turnaround, is_arrival = True))
        
    for time_from_b, time_to_a in b2a_l:
        #departure
        actions_l.append(my_action_c("B", time_from_b, is_arrival = False))

        #arrival (and ready for next departure)
        actions_l.append(my_action_c("A", time_to_a + time_turnaround, is_arrival = True))
    
    

    # sort all this:
    actions_l.sort(f_sort)


    nb_needed_in = {"A" : 0,
                    "B" : 0}
    
    nb_in = {"A" : 0,
             "B" : 0}
    
    # do all the actions:
    for action in actions_l:
        if _debug:
            print action

        if action.is_arrival:
            nb_in[action.where] += 1

        else: #departure
            if nb_in[action.where] <= 0: # no train ready !!
                nb_needed_in[action.where] += 1 # Take a new one
            else: # Some train already here, use it
                nb_in[action.where] -= 1
                
#        print nb_in, nb_needed_in


    return nb_needed_in["A"], nb_needed_in["B"]


def solve_case(case_no, turnaround, a2b_l, b2a_l):
    print "\n\n-------------- New case", case_no

    print "turnaround is %s min" % turnaround

    return "%d %d" % algo_complete(turnaround, a2b_l, b2a_l)

            
def main(argv):

    f_out = open(argv[1].split(".")[0] + ".out", "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):
        turnaround = int(fd.readline())

        na, nb = [int(item) for item in fd.readline().split()]

        a2b_l = []
        for na_line in range(na):
            a2b_l.append( tuple([get_time(item) for item in fd.readline().split()]) )
            

        b2a_l = []
        for nb_line in range(nb):
            b2a_l.append( tuple([get_time(item) for item in fd.readline().split()]) )

        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, turnaround, a2b_l, b2a_l)
                                         )
                     )
        f_out.flush()


    

import sys
if __name__ == "__main__":
    main(sys.argv)

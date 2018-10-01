from math import *
from random import *


###################################################################
##################### Round 1: Misc Funcions ######################
###################################################################


############### law_of_cosines  ###################################


def law_of_cosines(a, b, c):
    """ uses the law of cosines to return an angle using 3 triangle lengths """
    
    cos_gamma = (a**2 + b**2 - c**2) / (2*a*b)
    return acos(cos_gamma)*180/pi



###################################################################
##################### Round 1: Problem A ##########################
###################################################################

def arrange_problem_a(word_list):
    """ arranges the data for problem_a """
    
    num_cases = int(word_list[0])
    
    arranged_list = []
    word_iter = 1
    
    for case in range(num_cases):
        new_case = []
        coords_num = int(word_list[word_iter])
        word_iter += 1
        
        first_line = word_list[word_iter:word_iter+coords_num]
        word_iter += coords_num
        second_line = word_list[word_iter: word_iter+coords_num]
        word_iter += coords_num
        new_case.append(first_line)
        new_case.append(second_line)
        
##        ## maybe some stuff here
##
##        ## possible counted stuff
##        counter1_item_num = nested_list[word_iter]*COUNTER1_THINGS_PER_LINE
##        counter_items = word_list[word_iter, word_iter+counter1_item_num]
##        new_case.append(counter1_items)
##        word_iter += counter1_item_num
##        
##        ## possible counted stuff
##        counter2_item_num = nested_list[word_iter]*COUNTER2_THINGS_PER_LINE
##        counter2_items = word_list[word_iter, word_iter+counter2_item_num]
##        new_case.append(counter2_items)
##        word_iter += counter2_item_num       
    
    
        arranged_list.append(new_case)

        
    return arranged_list



def problem_a_main(arranged_message):
    """problem a's main computations"""
    
    case_num = 1
    for case in arranged_message:
        vector1 = sorted([int(x) for x in case[0]])
        vector2 = sorted([int(x) for x in case[1]])
        coords_num = len(case[0])
        total = 0
        for coord in range(coords_num):
            additive = int(vector1[coord])*int(vector2[coords_num-coord-1])
            total += additive

        print "Case #%s:" % case_num, total
        case_num +=1



def problem_a(raw_string):
    problem_a_main(arrange_problem_a(raw_string.split()))
    
        



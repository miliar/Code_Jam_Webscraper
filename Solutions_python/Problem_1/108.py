#! /usr/bin/python

##### Search engine switch problem
##### performed by ccarrico@gmail.com on July 16th, 2008, ~11 PM UTC
##### Python 2.5 running on Mac OS 10.4

def get_continuance_array( input_engines, input_queries ):

    qlen = len(input_queries) # it comes up a lot.
    
    current_max_position = [qlen for j in input_engines]
    cont_array = [[0.0 for k in input_queries] for j in input_engines]

    for k in range(qlen):
        for j in range(len(input_engines)):
            if input_engines[j] == input_queries[-1 -k]:
                current_max_position[j] = qlen - (1+k)
            cont_array[j][qlen - (1 + k)] = current_max_position[j]

    return cont_array

def get_n_switches( input_engines, input_queries ):

    continuance_array = get_continuance_array( input_engines, input_queries )
        
    print "\n".join(["\t".join([str(y) for y in x]) for x in continuance_array])# debug

    current_position = 0
    nswitches = -1 # so that when we pick the first engine, we set nswitches = 0
    current_engine = -1

    while current_position < len(input_queries):
        available_engine_effectiveness = [x[current_position] for x in continuance_array]
        current_position = max(available_engine_effectiveness) # pick the one that gets us the farthest
        current_engine = available_engine_effectiveness.index(current_position)
        nswitches = nswitches + 1

    return max([nswitches, 0])



##########
#  MAIN  #
##########
import sys

if len(sys.argv) != 3:
    print 'Please use the following syntax:'
    print '  [./search_engine_switch.py] [input_file_name] [output_file_name]'
    sys.exit()
    
input_file_data = file(sys.argv[1]).read().split("\n")

n_cases = int(input_file_data[0])
file_progress = 1
n_cases_done = 0

out_handle = file(sys.argv[2], 'w')

while n_cases_done < n_cases:

    # load search engine names
    n_search_engines = int(input_file_data[file_progress])
    search_engines = input_file_data[file_progress + 1: file_progress + 1 + n_search_engines]
    file_progress = file_progress + 1 + n_search_engines
    print n_search_engines, search_engines

    # load queries
    n_queries = int(input_file_data[file_progress])
    queries = input_file_data[file_progress + 1: file_progress + 1 + n_queries]
    file_progress = file_progress + 1 + n_queries
    print n_queries, queries

    out_string = 'Case #' + str(n_cases_done + 1) + ': ' + str(get_n_switches(search_engines, queries)) + "\n"
    out_handle.write(out_string)
    print out_string # dual output for easy debugging.  Hooray!

    # move on to next case
    n_cases_done = n_cases_done + 1

out_handle.close()

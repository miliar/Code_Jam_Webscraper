#!/usr/bin/python

# Cookie Problem for the Goggle Code Jam
# Emilio Unda <unda91@gmail.com>

import sys

INITIAL_PRODUCTION = 2.0

def cookies(infilename, outfilename) :
    file = open(infilename, "r")
    out = open(outfilename, "w")

    testcases = int(file.readline().strip())
    for i in range(testcases) :
        words = file.readline().split()
        # solve problem
        time = minimum_time(float(words[0]), 
                            float(words[1]),
                            float(words[2]))

        # do output 
        out.write("Case #{0}: {1:.7f}\n".format(i+1, time) )
    #end for
    file.close()
    out.close()
    return
    
def time_to_make_n_cookies(cookie_production, objective):
    return objective / cookie_production
        
def time_to_finish(cookies, cookie_production, objective):
    return time_to_make_n_cookies(objective - cookies, objective)

      
def minimum_time(farm_price, farm_production, objective):
    stop = False

    times_to_n_farms = [0.0]
    production_n_farms = [INITIAL_PRODUCTION]
    times_to_finish = []
    times_to_finish.append( time_to_make_n_cookies(production_n_farms[0],
                                                   objective) )
    i = 1;

    while not stop :
        # how much time to make the next farm
        times_to_n_farms.append(times_to_n_farms[i-1] + 
                                time_to_make_n_cookies(production_n_farms[i-1], 
                                                       farm_price))
        # the production rate after making i farms
        production_n_farms.append( production_n_farms[i-1] + farm_production )
        # time to finish if we make i farms
        times_to_finish.append( times_to_n_farms[i] + 
                                time_to_make_n_cookies(production_n_farms[i],
                                                       objective) )
        # next cycle 
        if times_to_finish[i] < times_to_finish[i-1]:
            i += 1
        # finish
        else :
            stop = True
    #end while
    result = times_to_finish[i-1];
    return result

    
def main(argv) :
    cookies(argv[1], argv[2])

if __name__ == "__main__" :
    main(sys.argv)

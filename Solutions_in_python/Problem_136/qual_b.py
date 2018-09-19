#!/usr/bin/env python2.7
#
# GoogleCodeJam 2014
# Qualification Round
# B - Cookie Clicker Alpha
#
# Edward Lau
# eplau[at]ucla[dot]edu
# 2014.04.12






######################
## IMPORT LIBRARIES ##
######################
import sys





##################
## SUBFUNCTIONS ##
##################
def timeCalc(goal, base, nF, Fbonus):
     return float(goal)/(base+nF*Fbonus)

def time4farms(n_farms, farm_cost, base, farm_bonus):
#    print "{} {} {} {}".format(n_farms, farm_cost, base, farm_bonus);
    if n_farms > 1:
        return time4farms(n_farms-1, farm_cost, base, farm_bonus) + timeCalc(farm_cost, base, n_farms-1, farm_bonus);
    elif n_farms == 1:
        return timeCalc(farm_cost, base, 0, farm_bonus);
    else:
        return 0;





##############
## FILENAME ##
##############
debug = True; # true == extra info output
debug = False;
input_file = sys.argv[1];

try:
    f_handle = open(input_file, 'r');
except:
    print "Does that file exist?"
    raise





#############
## N Cases ##
#############
n_cases = int(f_handle.readline().strip());
sys.setrecursionlimit(5000);
for i_case in range(0, n_cases):
    # Read row and settle the parts out
    row = f_handle.readline().strip().split();

    farm_cost = float(row[0]);
    farm_bonus = float(row[1]);
    goal = float(row[2]);

    if debug:
        print "C: {}\nF: {}\nX: {}\n".format(farm_cost, farm_bonus, goal);


    total_time = 0;
    straight_time = 1;
    build_time = 0;
    n_farms = 0;
    base = 2;

    while ( straight_time > build_time ):
        straight_time = time4farms(n_farms, farm_cost, base, farm_bonus) + timeCalc(goal, base, n_farms, farm_bonus);

        n_farms += 1;
        build_time = time4farms(n_farms, farm_cost, base, farm_bonus) + timeCalc(goal, base, n_farms, farm_bonus);

        if debug:
            print "{} vs {}".format(straight_time, build_time);

    # Print output
    print "Case #{}: {}".format(i_case+1, straight_time);





# Close out
f_handle.close();
